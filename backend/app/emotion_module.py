from deepface import DeepFace


def analyze_emotion(frame):

    try:

        result = DeepFace.analyze(
            img_path=frame,
            actions=["emotion"],
            detector_backend="retinaface",
            enforce_detection=True
        )


        if isinstance(result, list):
            result = result[0]


        emotion = result.get(
            "dominant_emotion",
            "unknown"
        )


        return {

            "emotion": emotion,

            "message":
            emotion_message(emotion)

        }


    except Exception as error:


        print(
            "Error emoción:",
            error
        )


        return {

            "emotion":
            "unknown",

            "message":
            "No se pudo analizar la emoción."

        }




def emotion_message(emotion):


    messages = {


        "happy":
        "Excelente actitud 😄. Que tengas un gran día.",


        "sad":
        "Ánimo 💪. Todo esfuerzo cuenta.",


        "angry":
        "Respira y mantén la calma 🙂.",


        "surprise":
        "¡Qué sorpresa verte hoy! 😮",


        "fear":
        "Todo estará bien. Sigue adelante.",


        "neutral":
        "Listo para comenzar. Buen día."

    }


    return messages.get(
        emotion,
        "Bienvenido al sistema."
    )