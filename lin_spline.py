#------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt


def prepare_input(x,y, axis):
    x, y = map(np.asarray, (x,y))
    if x.ndim != 1:
        raise ValueError("x must be 1d")
    if x.shape[0] < 2:
        raise ValueError("x must have at least two points")

def linear_spline(x, y, xp, axis=None):
    """ a linear interpolating polynomial between given points,
    currently along one dimension """
    x = np.asarray(x)
    y = np.asarray(y)
    xp = np.asarray(xp)
    n = len(xp)
    yp = np.zeros((n,))
    if len(x) != len(y):
        raise ValueError("x and y should be of same length")
    m = np.ndarray((n,))
    for i in range(n):
        m[i] = (y[i+1] - y[i])/(x[i+1] - x[i])
        if x[i]<=xp[i]<=x[i+1]:
            yp[i] = y[i] + m[i]*(xp[i] - x[i])
        elif xp[i]<x[i]:
            raise ValueError("out of bounds")
        else:
            continue
    plt.scatter(xp,yp, color="orange", label="interpolated points")
    plt.plot(xp,yp,color="orange")
    plt.plot(x,y)
    plt.scatter(x,y)
    plt.legend()
    plt.show()
    return (yp)

"""example1 : the lesser number of points you take to interpolate, the lesser acuurate your result is"""

print(linear_spline([0,1,2,3,4], [5,9,7,6,8], [0.5,1.5,2.75]))
