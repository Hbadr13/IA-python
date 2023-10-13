import numpy as np


class ScrapBooker:
    def __init__(self):
        pass

    def crop(self, array, dim, position=(0, 0)):
        if self.checkParameters(array, 1) == False or self.checkParameters(dim, 2) == False or self.checkParameters(position, 2) == False:
            return None
        if position[0] > array.shape[0] or position[1] > array.shape[1]:
            return None
        if position[0] < 0 or position[1] < 0:
            return None
        if array.shape[0] - position[0] < dim[0]:
            return None
        if array.shape[1] - position[1] < dim[1]:
            return None
        return array[position[0]:dim[0] + 1, position[1]:dim[1]]

    def thin(self, array, n, axis):
        if self.checkParameters(array, 1) == False or self.checkParameters(n, 3) == False or self.checkParameters(axis, 4) == None:
            return None
        if axis == 0:
            list_of_index = [i for i in range(
                0, array.shape[1]) if (i + 1) % n == 0]
            return np.delete(array, list_of_index, axis=not axis)
        elif axis == 1:
            list_of_index = [i for i in range(
                0, array.shape[0]) if (i + 1) % n == 0]
            return np.delete(array, list_of_index, axis=not axis)

    def juxtapose(self, array, n, axis):
        if self.checkParameters(array, 1) == False or self.checkParameters(n, 3) == False or self.checkParameters(axis, 4) == False:
            return None
        if not isinstance(n, int) or not isinstance(axis, int):
            return None
        if axis != 0 and axis != 1:
            return None
        if axis == 0:
            return np.array(np.tile(array, (n, 1)))
        if axis == 1:
            return np.array(np.tile(array, (1, n)))

    def mosaic(self, array, dim):
        if self.checkParameters(array, 1) == False or self.checkParameters(dim, 2) == False:
            return None
        return np.array(np.tile(array, dim))

    def checkParameters(self, varaible, status):
        if status == 1:
            if not isinstance(varaible, np.ndarray):
                return False
        if status == 2:
            if not isinstance(varaible, tuple):
                return False
            if len(varaible) != 2:
                return False
            if not isinstance(varaible[0], int) or not isinstance(varaible[1], int):
                return False
        if status == 3 or status == 4:
            if not isinstance(varaible, int):
                return False
        if status == 4:
            if varaible != 1 and varaible != 0:
                return False