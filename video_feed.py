# video_feed.py
import cv2
import numpy as np
from tensorflow.keras.models import load_model

class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.model = load_model("facial_expression_model.h5")
        self.emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()
        if not ret:
            return b''

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (48, 48))
            face = face.astype("float") / 255.0
            face = np.expand_dims(face, axis=0)
            face = np.expand_dims(face, axis=-1)
            prediction = self.model.predict(face, verbose=0)
            label = self.emotion_labels[np.argmax(prediction)]

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (255, 255, 255), 2)

        _, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
