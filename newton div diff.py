

import numpy as np

def p(x, y):
    x = np.asarray_chkfinite(x)
    y = np.asarray_chkfinite(y)
    n = len(y)
    #x = np.ndarray((2*(n-1),1))
    for i in range(n-1):
        y[i] = (y[i+1] - y[i])/ (x[i+1] - x[i])
        print(x[i],y[i])
       # x1[2*i] = x[i]

    return (y,x)

    #x_t = np.zeros((2*n-2,n-1))

    #for i in range(n-1):
       # x_t[2*i][0] = x[i]
        #x_t[2*i + 1][0] = x[i+1]


p([0,1,2,4,5,6],[1,14,15,5,6,19])


