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

    # faceList = []

    # for file in os.listdir(args.images):
    #     if file.endswith(".jpg"):
    #         temp_Image = Image(args.images + "/" + file)
    #         faceList.append(Face(temp_Image))

    # for face in faceList:
    #     face.show()

    #TODO: Download predictor and set path (https://www.pyimagesearch.com/2017/04/10/detect-eyes-nose-lips-jaw-dlib-opencv-python/)
    path_to_shape_predictor = ""

    # init dlib's face detector (HOG-based) and then create the facial landmark predictor
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(path_to_shape_predictor)

    # load input image
    img = Image("~/Pictures/PicOfTheDay-Testing/IMG_20190911_210847.jpg")
    img = imutils.resize(img.get(), width=500)
    gray = cv2.cvtColor(img.get(), cv2.COLOR_BGR2GRAY)

    #detect faces in grayscale image
    rects = detector(gray, 1)

if __name__ == "__main__":
    main()
