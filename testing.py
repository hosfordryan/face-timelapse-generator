import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
import imutils
from image import Image
from face import Face
from imutils import face_utils
import dlib

def main():
    parser = argparse.ArgumentParser(description="Program to create timelapses of faces using facial landmark detection.")
    parser.add_argument('images', metavar='i', help='Path to folder containing images')
    parser.add_argument('-o','--output', help='name of output video')
    parser.add_argument('-s','--speed',type=int, default=100, help='milliseconds between frames in timelapse')

    args = parser.parse_args()

    faceList = []

    for file in os.listdir(args.images):
        if file.endswith(".jpg"):
            temp_Image = Image(args.images + "/" + file)
            faceList.append(Face(temp_Image))

    for face in faceList:
        face.detectFeatures()
        #face.show()
        print(face.left_eye)
        print(face.right_eye)
        print(face.eye_midpoint)
        print(face.nose)

    


def landmarkTesting():
    path_to_shape_predictor = "shape_predictor_5_face_landmarks.dat"

    # init dlib's face detector (HOG-based) and then create the facial landmark predictor
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(path_to_shape_predictor)

    # load input image
    #img = Image("~/Pictures/PicOfTheDay-Testing/IMG_20190911_210847.jpg")
    img = Image("testImage.jpg")
    img = imutils.resize(img.image, width=500)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detect faces in grayscale image
    rects = detector(gray, 1)

    #loop over the face detections
    for (i, rect) in enumerate(rects):
        #determine the facial landmarks for the face region, then convert coords to NumPy array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        #clone original image so we can draw on it
        clone = img.copy()

        #loop over the face parts individually
        for (i, (x, y)) in enumerate(shape):
            
            #cv2.putText(clone, i, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            
            #Draw dots for each
            cv2.circle(clone, (x, y), 1, (0, 0, 255), -1)


        #show the face
        cv2.imshow("IMAGE", clone)
        cv2.waitKey(0)

if __name__ == "__main__":
    main()
