import base64
import cv2
import numpy as np

from deepface import DeepFace



def decode_base64_image(image_base64: str):

    if not image_base64:
        raise ValueError("Imagen vacía")


    if "," in image_base64:
        image_base64 = image_base64.split(",", 1)[1]


    try:

        image_bytes = base64.b64decode(
            image_base64
        )

    except Exception:

        raise ValueError(
            "Imagen base64 inválida"
        )



    array = np.frombuffer(
        image_bytes,
        np.uint8
    )


    frame = cv2.imdecode(
        array,
        cv2.IMREAD_COLOR
    )


    if frame is None:

        raise ValueError(
            "No se pudo procesar la imagen"
        )


    return frame






def get_first_face_encoding(image_base64: str):


    frame = decode_base64_image(
        image_base64
    )


    result = DeepFace.represent(

        img_path=frame,

        model_name="Facenet",

        detector_backend="retinaface",

        enforce_detection=True

    )


    if not result:

        raise ValueError(
            "No se detectó rostro"
        )


    return result[0]["embedding"]






def get_face_embedding(frame):


    result = DeepFace.represent(

        img_path=frame,

        model_name="Facenet",

        detector_backend="retinaface",

        enforce_detection=True

    )


    if not result:

        raise ValueError(
            "No se detectó rostro"
        )


    return result[0]["embedding"]






def compare_faces(
    current_embedding,
    saved_embedding,
    threshold=10
):


    current = np.array(
        current_embedding
    )


    saved = np.array(
        saved_embedding
    )


    distance = np.linalg.norm(
        current - saved
    )


    return distance < threshold, distance






def detect_face(frame):


    try:


        result = DeepFace.extract_faces(

            img_path=frame,

            detector_backend="retinaface",

            enforce_detection=False

        )


        if result:

            return True


        return False



    except Exception:


        return False






def get_emotion_face(frame):

    """
    Extrae el rostro principal usando
    el mismo detector RetinaFace.

    Se utiliza para análisis emocional.
    """


    try:


        faces = DeepFace.extract_faces(

            img_path=frame,

            detector_backend="retinaface",

            enforce_detection=True

        )


        if not faces:

            return None



        face = faces[0]["face"]


        return face



    except Exception as error:


        print(
            "Error extracción rostro emoción:",
            error
        )


        return None