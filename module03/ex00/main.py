from NumPyCreator import NumPyCreator
npc = NumPyCreator()
import numpy as np

from collections.abc import Iterable


# if isinstance("1",Iterable):
    # print("problem")


# Output :
# array([[1, 2, 3],
#    [6, 3, 4]])


# a = npc.from_list([[1, 2, 3],[2,2]])

# create a 3D array
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# # get the number of dimensions and shape of the array
# ndim = arr.ndim
# shape = arr.shape

# # print the results
# print("Number of dimensions:", ndim)
# print("Shape of array:", shape)

# print (a)
# Output :
# None


# npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]])
# Output :
# array([['1', '2', '3'],
#    ['a', 'b', 'c'],
#    ['6', '4', '7'], dtype='< U21'])


# npc.from_list(((1, 2), (3, 4)))
# Output :
# None


# npc.from_tuple(("a", "b", "c"))
# Output :
# array(['a', 'b', 'c'])


# npc.from_tuple(["a", "b", "c"])
# Output :
# None


# npc.from_iterable(range(5))
# Output :
# array([0, 1, 2, 3, 4])

# shape = (3, 5)
# npc.from_shape(shape)
# Output :
# array([[0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0]])

# npc.identity(4)
# Output :
# array([[1., 0., 0., 0.],
#    [0., 1., 0., 0.],
#    [0., 0., 1., 0.],
#    [0., 0., 0., 1.]])
