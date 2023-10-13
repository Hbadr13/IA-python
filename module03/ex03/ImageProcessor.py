import numpy as np
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
import cv2
class ImageProcessor:
    def __init__(self):
        pass

    def load(self, filename):
        try:
            image = mpimg.imread(filename)
            print(f"Loading image of dimensions %d x %d"%(image.shape[0],image.shape[1]))
            return  image
        except Exception as e:
            print("Exception :", type(e).__name__, "-- strerror:", e)
    def display(self, array):
        try:
            if not isinstance(array, np.ndarray):
                raise ValueError("array must be an instance of np.array")
            # @ Method 1
            plt.axis('off')
            plt.imshow(array)
            plt.show()

            # @ Method 2
            # cv2.imshow('image', array)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

        except Exception as e:
            print("Exception :", type(e).__name__, "-- strerror:", e)   
