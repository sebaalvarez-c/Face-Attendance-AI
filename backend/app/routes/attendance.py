import json
from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from app import models, schemas
from app.database import get_db


from app.face_recognition_module import (
    decode_base64_image,
    detect_face,
    get_face_embedding,
    compare_faces
)


from app.geo_validation import validate_location


from app.emotion_recognition import analyze_emotion


from app.voice_recognition import recognize_voice



router = APIRouter(
    tags=["Attendance"]
)



# =====================================
# IDENTIFICAR USUARIO POR ROSTRO
# =====================================

def identify_user(db: Session, current_embedding):


    users = (

        db.query(models.User)

        .filter(
            models.User.face_encoding.isnot(None)
        )

        .all()

    )


    best_user = None
    best_distance = 999



    for user in users:

        try:


            saved_embedding = json.loads(
                user.face_encoding
            )


            match, distance = compare_faces(
                current_embedding,
                saved_embedding
            )


            if distance < best_distance:

                best_distance = distance
                best_user = user



        except Exception:

            continue




    if best_user and best_distance < 10:

        return best_user



    return None






# =====================================
# MARCAR ASISTENCIA
# =====================================


@router.post("/mark-attendance")
def mark_attendance(

    data: schemas.AttendanceRequest,

    db: Session = Depends(get_db)

):


    try:


        frame = decode_base64_image(
            data.image_base64
        )


    except Exception as exc:


        raise HTTPException(
            status_code=400,
            detail=str(exc)
        )




    # ===============================
    # 1. DETECTAR ROSTRO
    # ===============================


    if not detect_face(frame):


        return {

            "status":"error",

            "message":
            "No se detectó rostro."

        }






    # ===============================
    # 2. OBTENER EMBEDDING
    # ===============================


    try:


        embedding = get_face_embedding(
            frame
        )


    except Exception as exc:


        return {

            "status":"error",

            "message":str(exc)

        }






    # ===============================
    # 3. EMOCION
    # ===============================


    try:


        emotion_result = analyze_emotion(
            frame
        )


    except Exception as exc:


        print(
            "ERROR EMOCION:",
            exc
        )


        emotion_result = {

            "emotion":
            "No detectada",

            "message":
            "No se pudo analizar emoción"

        }






    # ===============================
    # 4. IDENTIFICAR USUARIO
    # ===============================


    user = identify_user(

        db,

        embedding

    )




    if not user:


        return {

            "status":"unknown",

            "message":
            "Rostro no reconocido.",

            "emotion":
            emotion_result["emotion"]

        }





    # ===============================
    # 5. VOZ
    # ===============================

    try:


        voice_result = recognize_voice()



    except Exception as exc:


        print(
            "ERROR VOZ:",
            exc
        )


        voice_result = {


            "valid":False,

            "text":
            "No reconocida"

        }




    # IMPORTANTE:
    # LA VOZ NO BLOQUEA

    if not voice_result.get("valid",False):


        print(
            "Voz no validada, continúa con facial"
        )


        voice_result["text"] = "No reconocida"






    # ===============================
    # 6. GPS
    # ===============================


    try:


        location = validate_location(

            data.lat,

            data.lng

        )


    except Exception as exc:


        print(
            "ERROR GPS:",
            exc
        )


        location = {


            "valid":True,

            "distance_meters":0

        }







    if not location["valid"]:


        return {


            "status":
            "out_of_range",


            "message":
            f"Fuera del rango permitido ({location['distance_meters']} m)",


            "emotion":
            emotion_result["emotion"]

        }






    # ===============================
    # 7. EVITAR DUPLICADOS
    # ===============================


    today = date.today()



    existing = (

        db.query(models.Attendance)

        .filter(

            models.Attendance.user_id == user.id,

            models.Attendance.attendance_date == today

        )

        .first()

    )




    if existing:


        return {


            "status":
            "duplicate",


            "message":
            f"{user.name} ya registró asistencia.",


            "emotion":
            emotion_result["emotion"],


            "voice":
            voice_result["text"]

        }







    # ===============================
    # 8. GUARDAR
    # ===============================



    attendance = models.Attendance(


        user_id=user.id,


        attendance_date=today,


        status="present",


        lat=data.lat,


        lng=data.lng,


        distance_meters=
        location["distance_meters"]


    )




    db.add(attendance)

    db.commit()

    db.refresh(attendance)






    return {


        "status":
        "success",


        "message":
        f"Asistencia registrada para {user.name}",


        "user":{


            "name":
            user.name,


            "code":
            user.code

        },


        "emotion":
        emotion_result["emotion"],


        "voice":
        voice_result["text"]


    }







# =====================================
# HISTORIAL
# =====================================


@router.get("/get-attendance")
def get_attendance(

    db: Session = Depends(get_db)

):


    records = (


        db.query(

            models.Attendance,

            models.User

        )


        .join(

            models.User,

            models.Attendance.user_id ==
            models.User.id

        )


        .order_by(

            models.Attendance.created_at.desc()

        )


        .all()


    )




    return [


        {


            "name":
            user.name,


            "code":
            user.code,


            "role":
            user.role,


            "date":
            attendance.attendance_date.isoformat(),


            "status":
            attendance.status,


            "distance":
            attendance.distance_meters


        }


        for attendance,user in records


    ]







# =====================================
# DASHBOARD
# =====================================


@router.get("/dashboard")
def dashboard(

    db: Session = Depends(get_db)

):


    total_users = db.query(
        models.User
    ).count()



    total_records = db.query(
        models.Attendance
    ).count()



    today = date.today()



    present_today = (

        db.query(models.Attendance)

        .filter(

            models.Attendance.attendance_date == today

        )

        .count()

    )




    history = (

        db.query(

            models.Attendance,

            models.User

        )


        .join(

            models.User,

            models.Attendance.user_id ==
            models.User.id

        )


        .order_by(

            models.Attendance.created_at.desc()

        )


        .all()

    )





    return {


        "stats":{


            "users":
            total_users,


            "records":
            total_records,


            "present_today":
            present_today


        },



        "history":[



            {


                "usuario":
                user.name,


                "codigo":
                user.code,


                "rol":
                user.role,


                "fecha":
                attendance.attendance_date.isoformat(),


                "estado":
                attendance.status,


                "distancia":
                attendance.distance_meters


            }


            for attendance,user in history


        ]

    }