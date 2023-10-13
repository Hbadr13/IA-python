from ScrapBooker import ScrapBooker
import numpy as np
import module03.ex03.ImageProcessor as ImageProcessor
obj = ImageProcessor.ImageProcessor()
# array = obj.load('42AI.png')
spb = ScrapBooker()
arr3 = np.array([1,2])
print(spb.mosaic(arr3, (3, 3)))

# print(spb.thin(arr2,3,0))
# print(spb.thin())
