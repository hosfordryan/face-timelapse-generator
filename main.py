import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
from image import Image
import dlib

def main():
    parser = argparse.ArgumentParser(description="Program to create timelapses of faces using facial landmark detection.")
    parser.add_argument('images', metavar='i', help='Path to folder containing images')
    parser.add_argument('-o','--output', help='name of output video')
    parser.add_argument('-s','--speed',type=int, default=100, help='milliseconds between frames in timelapse')

    args = parser.parse_args()

    imageList = []

    for file in os.listdir(args.images):
        if file.endswith(".jpg"):
            temp_Image = Image(args.images + "/" + file)
            imageList.append(temp_Image)

    for image in imageList:
        image.showImage()

if __name__ == "__main__":
    main()
