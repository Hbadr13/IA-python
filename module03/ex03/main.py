

from ImageProcessor import ImageProcessor



import numpy as np
imp = ImageProcessor()
# arr = imp.load("assets/42AI.png")
arr = imp.load("assets/elon_canaGAN.png")
# arr = imp.load("assets/m.jpg")

from ColorFilter import ColorFilter
cf = ColorFilter()

# print(cf.to_celluloid(arr))
imp.display(cf.to_grayscale(arr,"w"))
