import cv2
import numpy as np
from image import Image
import dlib
import imutils
from imutils import face_utils
class Face:

    def __init__(self, image):
        self.image = image

    def show(self):
        self.image.showImage()

    def detectFeatures(self):
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("shape_predictor_5_face_landmarks.dat")


        img = self.image
        #convert img to grayscale
        gray = cv2.cvtColor(img.image, cv2.COLOR_BGR2GRAY)

        #detect faces in the image
        faces = detector(gray, 1)

        #If we detected a face
        if len(faces) > 0:

            #loop over the face detections
            for (i, face) in enumerate(faces):
                #find the facial landmarks and convert to Numpy array
                landmarks = predictor(gray, face)
                landmarks = face_utils.shape_to_np(landmarks)

                self.right_eye = (landmarks[0],landmarks[1])
                self.left_eye = (landmarks[2], landmarks[3])
                self.nose = landmarks[4]

