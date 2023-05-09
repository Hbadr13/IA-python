class Vector:
    def __init__(self, vect):
        if isinstance(vect, int):
            lst = []
            for i in range(0, vect):
                l = []
                l.append(float(i))
                lst.append(l)
            if len(lst) != 0:
                self.values = lst
                self.shape = (vect, 1)
            else:
                self.values = [[]]
                self.shape = (0, 0)
            return
        elif isinstance(vect, tuple) and len(vect) == 2 and isinstance(vect[0], int) and isinstance(vect[1], int):
            if vect[0] > vect[1]:
                raise NotImplemented("")
            lst = []
            for i in range(vect[0], vect[1]):
                l = []
                l.append(float(i))
                lst.append(l)
            if len(lst) != 0:
                self.values = lst
                self.shape = (vect[1] - vect[0], 1)
            else:
                self.values = [[]]
                self.shape = (0, 0)
            return
        else:
            self.shape = (len(vect), len(vect[0]))
            self.values = vect
            if self.shape[0] != 1:
                for lst in self.values:
                    if len(lst) != 1:
                        raise ValueError(
                            "The vector shape should be on the figure (1,n) or (n,1)")
            for lst in self.values:
                for elm in lst:
                    if type(elm) != float:
                        # pass
                        raise ValueError(
                            "The vector type should be list of list float only")

    def __str__(self):
        return str(self.values)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ValueError(
                "this variable must be a Vector of dimensions (1,n) or (n,1)")
        if self.shape != other.shape:
            raise ValueError(
                "dimensions of this variable must match dimensions of other")
        lst = []
        for lst1, lst2 in zip(self.values, other.values):
            l = []
            for i, j in zip(lst1, lst2):
                l.append(i + j)
            lst.append(l)
        return Vector(lst)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise ValueError(
                "this variable must be a Vector of dimensions (1,n) or (n,1)")
        if self.shape != other.shape:
            raise ValueError(
                "dimensions of this variable must match dimensions of other")
        lst = []
        for lst1, lst2 in zip(self.values, other.values):
            l = []
            for i, j in zip(lst1, lst2):
                l.append(i - j)
            lst.append(l)
        return Vector(lst)

    def __rsub__(self, other):
        if not isinstance(other, Vector):
            raise ValueError(
                "this variable must be a Vector of dimensions (1,n) or (n,1)")
        if self.shape != other.shape:
            raise ValueError(
                "dimensions of this variable must match dimensions of other")
        lst = []
        for lst1, lst2 in zip(other.values, self.values):
            l = []
            for i, j in zip(lst1, lst2):
                l.append(i - j)
            lst.append(l)
        return Vector(lst)

    def __mul__(self, other):
        # if type(other) != float:
        # raise ValueError("The vector * float.")
        return [[elm*other for elm in lst] for lst in self.values]

    def __rmul__(self, other):
        # if type(other) != float:
        # raise ValueError("The vector * float.")
        return [[elm*other for elm in lst] for lst in self.values]

    def __truediv__(self, other):
        # if type(other) != float:
        # raise ValueError("The vector * float.")
        if other == 0:
            raise ZeroDivisionError("division by zero.")
        return [[elm/other for elm in lst] for lst in self.values]

    def __rtruediv__(self, other):
        raise NotImplementedError(
            "Division of a scalar by a Vector is not defined here.")

    def T(self):
        # <===># lst = zip(self.values[0],self.values[1])
        tar = zip(*self.values)
        lst = []
        for line in tar:
            row = list(line)
            lst.append(row)
        return Vector(lst)

    def dot(self, other):
        if not isinstance(other, Vector):
            raise ValueError(
                "this variable must be a Vector of dimensions (1,n) or (n,1)")
        if self.shape != other.shape:
            raise ValueError(
                "dimensions of this variable must match dimensions of other")
        some = 0
        for lst1, lst2 in zip(self.values, other.values):
            for i, j in zip(lst1, lst2):
                some += i*j
        return some
