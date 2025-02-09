import face_recognition
import cv2

def recognize_face(image_path):
    try:
        # Load the image
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)

        if face_locations:
            print("Face detected!")
            face_encoding = face_recognition.face_encodings(image)[0]
            return {"status": "success", "face_encoding": face_encoding.tolist()}
        else:
            print("No face detected.")
            return {"status": "error", "message": "No face detected"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
