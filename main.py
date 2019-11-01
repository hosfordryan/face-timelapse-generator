import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
from image import Image
from face import Face
import dlib
from functools import cmp_to_key


# TODO: Need to implement
def main():
    parser = argparse.ArgumentParser(description="Program to create timelapses of faces using facial landmark detection.")
    parser.add_argument('images', metavar='i', help='Path to folder containing images')
    parser.add_argument('-o','--output', help='name of output video')
    parser.add_argument('-s','--speed',type=int, default=100, help='milliseconds between frames in timelapse')

    args = parser.parse_args()

    #Need to open the images in order, so read names and sort 
    files = []
    for file in os.listdir(args.images):
        if file.endswith(".jpg"):
            files.append(file)
    #print(files)
    #sort filenames using defined comparison function
    files = sorted(files,key=lambda name: int(name.split('_')[1]))
    print(files)
    # count = 0
    # for file in os.listdir(args.images):
    #     if file.endswith(".jpg"):
    #         face = Face(Image(args.images + "/" + file))
    #         print("Size of {}: {}".format(face.image.path,face.image.image.shape))


def filename_comparison(x,y):
    return int(x.split('_')[1]) - int(y.split('_')[1])

if __name__ == "__main__":
    main()
