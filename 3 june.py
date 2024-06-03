#-------------------------------------------------------------------------------


import numpy as np

class Matrix():
    def __init__(self,zyarr):
        self.zyarr = np.asarray(zyarr)
        if self.zyarr.ndim != 2:
            raise ValueError
        self.n = len(self.zyarr[0])
        self.v = np.zeros((self.n,self.n))

    def make(self):
        col = []
        for i in range(self.n):
            for z in self.zyarr[0]:
                c = z**i
                col.append(c)
            col = np.asarray(col)
            self.v[:,i] = col
            col = []

        return self.v


    def yvals(self):
        self.y = np.array(self.zyarr[1])
        self.y = self.y.reshape((self.n,1))
        return self.y


m = Matrix([[3,4,5], [4,5,6]])

print(m.make())
print(m.n)

print(m.yvals())

