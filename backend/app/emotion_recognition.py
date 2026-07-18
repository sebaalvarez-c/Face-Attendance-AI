from deepface import DeepFace
import cv2
import numpy as np


def analyze_emotion(frame):

    try:

        print("=== INICIO EMOCION ===")


        # asegurar formato correcto

        if frame.dtype != np.uint8:

            frame = frame.astype(
                np.uint8
            )


        result = DeepFace.analyze(

            img_path=frame,

            actions=[
                "emotion"
            ],

            detector_backend="retinaface",

            enforce_detection=False,

            silent=True

        )


        if isinstance(result,list):

            result=result[0]


        emotion = result.get(
            "dominant_emotion",
            "unknown"
        )


        print(
            "EMOCION:",
            emotion
        )


        return {

            "emotion":
            emotion,

            "message":
            emotion_message(
                emotion
            )

        }



    except Exception as e:


        print(
            "ERROR EMOCION:",
            e
        )


        return {

            "emotion":
            "unknown",

            "message":
            "No se pudo analizar emoción."

        }




def emotion_message(emotion):


    mensajes={


        "happy":
        "Excelente actitud 😄",


        "neutral":
        "Listo para comenzar 👍",


        "sad":
        "Ánimo, sigue adelante 💪",


        "angry":
        "Mantén la calma 🙂",


        "surprise":
        "Qué sorpresa 😮",


        "fear":
        "Todo estará bien"

    }


    return mensajes.get(

        emotion,

        "Bienvenido"

    )