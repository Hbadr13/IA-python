import functools
import math
# source https://towardsdatascience.com/what-are-quartiles-c3e117114cf1
# video  :https://www.youtube.com/watch?v=XZMwKI6YgLM


class TinyStatistician:
    def __init__(self):
        pass
    # @staticmethod

    def checkArgIsValid(self, var):
        if not isinstance(var, list):
            return None
        for i in var:
            if not isinstance(i, int):
                return None
        if len(var) == 0:
            return None
        return True

    def mean(self, x):
        if self.checkArgIsValid(x) == None:
            return None
        some = functools.reduce(lambda x, y: x + y, x)
        return some / len(x)

    def median(self, x):
        if self.checkArgIsValid(x) == None:
            return None
        cpy = x.copy()
        cpy.sort()
        if len(cpy) % 2 == 1:
            return cpy[int(len(cpy)/2)]
        else:
            return (cpy[int(len(cpy)/2)] + cpy[int(len(cpy)/2) - 1]) / 2

    def quartiles(self, x):
        if self.checkArgIsValid(x) == None:
            return None
        data = x.copy()
        data.sort()
        lst = []
        if len(data) % 2 == 0:
            q1 = self.median(data[:-(int(len(data)/2 - 1))])
            if len(data) == 2:
                q1 = self.median(data)
            q2 = self.median(data[(int(len(data)/2 - 1)):])
            lst.append(q1)
            lst.append(q2)
        else:
            q1 = self.median(data[:-(int(len(data)/2))])
            if len(data) == 1:
                q1 = data[0]
            q2 = self.median(data[(int(len(data)/2)):])
            lst.append(q1)
            lst.append(q2)
        return lst
    def var(self, x):
        if self.checkArgIsValid(x) == None:
            return None
        nu = self.mean(x)
        sum = 0.0
        for elm in x:
            sum += (elm - nu)**2
        return sum/len(x)
    
    def std(self, x):
        if self.checkArgIsValid(x) == None:
            return None
        var = self.var(x)
        return math.sqrt(var)