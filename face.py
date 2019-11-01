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

                #Find midpoint of eye landmarks
                self.right_eye = [(landmarks[0][0] + landmarks[1][0]//2), (landmarks[0][1]+landmarks[1][1])//2]
                self.left_eye = [(landmarks[2][0] + landmarks[3][0])//2, (landmarks[2][1]+landmarks[3][1])//2]
                self.eye_midpoint = [(self.right_eye[0] + self.left_eye[0])//2, (self.right_eye[1] + self.left_eye[1]) //2]

                #Compute angle between eyes
                dY = self.right_eye[1] - self.left_eye[1]
                dX = self.right_eye[0] - self.left_eye[0]
                self.eye_angle = np.degrees(np.arctan2(dY, dX)) - 180
                self.nose = landmarks[4]
    

