import cv2
import matplotlib.pyplot as plt

class Image:
    #Constructor. Path is the only attribute that can be passed in creation
    def __init__(self, path):
        self.path = path
        self.image = None
        self.load()

    # Load the image
    def load(self):
        if self.path is None:
            raise ValueError('No path set for object.')
        self.image = cv2.imread(self.path)

    # Setter for path attribute
    def setPath(self, path):
        self.path = path

    # Show the image
    def showImage(self):
        plt.imshow(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
        plt.show()

    #not needed. just do Image.image
    def get(self):
        return self.image