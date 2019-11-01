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
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

        self.features = []

        img = self.image
        #convert img to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #detect faces in the image
        faces = detector(gray, 1)

        #loop over the face detections
        for (i, face) in enumerate(faces):
            #find the facial landmarks and convert to Numpy array
            landmarks = predictor(gray, face)
            landmarks = face_utils.shape_to_np(face)

            #add the parts to the list
            for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
                print("Not done")

