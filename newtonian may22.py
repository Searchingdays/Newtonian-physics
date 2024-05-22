#---------------------------------------------------------------------------
#-------------------------------------------------------------------------------

class body:
    """ initial state of the
    body """
    def __init__(self,mass, v: tuple):
        #self.m = mass
        self.vx = v[0]
        self.vy = v[1]
        self.vz = v[2]
        self.px = m*v[0]
        self.py = m*v[1]
        self.pz = m*v[2]

    """ force on the body"""

    def f_on(self,fx,fy,fz):
        self.fx = fx
        self.fy = fy
        self.fz = fz

def time():
    return t

def mass(self,a,b,c,d,e):
    self.m = a*t^4 + b*t^3 + c*t^2 + d*t + e

c = body(2,(3,4,3))

mass(2,3,4,5,6,5)





