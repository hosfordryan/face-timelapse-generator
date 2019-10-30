import cv2
import numpy as np
from image import Image
class Face:

    def __init__(self, image):
        self.image = image

    def show(self):
        self.image.showImage()

