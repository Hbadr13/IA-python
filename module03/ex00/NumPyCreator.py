import numpy as np
import random
from collections.abc import Iterable


class NumPyCreator:
    def __init__(self):
        pass

    def from_list(self, lst):
        if not isinstance(lst, list):
            return None
        #
        #

        #   big problem here: if you want to create a NumPy
        #   [[1,2,3],[2,3]] this is problem becouse len([1,2,3]) != len([2,3])

        #
        #
        array = np.array(lst, dtype="object")
        print(array.shape)
        print(array.ndim)
        return array

    def from_tuple(self, tpl):
        if not isinstance(tpl, tuple):
            return None
        return np.array(tpl)

    def from_iterable(self, itr):
        if not isinstance(itr, range):
            return None
        return np.array(itr, dtype=np.int16)

    def from_shape(self, shape=None, value=0):
        if not isinstance(shape, tuple) or len(shape) != 2:
            return None
        if not isinstance(value, int) or not isinstance(shape[0], int) or not isinstance(shape[1], int):
            return None
        if shape[0] < 0 or shape[1] < 0:
            return None
        lst = [[value for _ in range(shape[1])] for _ in range(shape[0])]
        return np.array(lst, dtype=np.int16)

    def random(self, shape):
        if not isinstance(shape, tuple) or len(shape) != 2:
            return None
        if not isinstance(shape[0], int) or not isinstance(shape[1], int):
            return None
        if shape[0] < 0 or shape[1] < 0:
            return None
        lst = [[random.random() for _ in range(shape[1])]
               for _ in range(shape[0])]
        return np.array(lst, dtype=np.int16)

    def identity(self, n):
        if not isinstance(n, int):
            return None
        lst = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
        return np.array(lst, dtype=np.int16)
