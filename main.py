import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

parser = argparse.ArgumentParser(description="Program to create timelapses of faces using facial landmark detection.")
parser.add_argument('images', metavar='i', help='Path to folder containing images')
parser.add_argument('-o','--output', help='name of output video')
parser.add_argument('-s','--speed',type=int, default=100, help='milliseconds between frames in timelapse')

args = parser.parse_args()

for file in os.listdir(args.images):
    if file.endswith(".jpg"):
        print(file)
        test_image = cv2.imread(file)
        image_grey = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

        plt.imshow(image_grey, cmap='grey')


