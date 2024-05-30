#-------------------------------------------------------------------------------


import math
import numpy as np

import matplotlib.pyplot as plt

class series():
    def __init__(self,x,n):
        self.x = x
        self.n = n


    def f(self):
        s = 0
        l = []
        ax = []
        for i in range(self.n):
            s = s + (self.x**(2*i))/math.factorial(i)
            l.append(s)
            ax.append(i)
        self.l = l
        self.s = s
        self.ax = ax

        return s,l


two = series(2,20)
th = series(3,20)
fo = series(4,20)
fi = series(5,8)

two.f()
th.f()
fo.f()
fi.f()

def compare(x,n):
    l = []
    r = []
    ax = []
    for i in range(n+1):
        l.append(math.factorial(i))
        r.append(x**(2*i))
        ax.append(i)
    plt.scatter(ax,l,label="factorial n")
    plt.scatter(ax,r, label="x^2n")
    plt.legend()
    plt.show()
    return l,r

plt.scatter(two.ax,two.l,label="x=2")
plt.ylim(-200,1000)
plt.scatter(th.ax,th.l, label="x=3")
plt.scatter(fo.ax,fo.l, label="x=4")
plt.scatter(fi.ax,fi.l, label="x=5")
plt.title(label ="the series (sum) from i=0 to i=n x^(2*n)/n!")
plt.legend()

#print(compare(2,20))
plt.show()



