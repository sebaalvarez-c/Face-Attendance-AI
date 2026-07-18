from deepface import DeepFace

def create_embedding(image):
    result = DeepFace.represent(img_path=image, model_name="Facenet")
    return result[0]["embedding"]
