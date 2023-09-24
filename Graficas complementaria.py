import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

t=np.linspace(0,8,15)

g=-9.8
y0=0
v0=0

def posicion(y0, v0, a, t):
    return y0+v0*t+(1/2)*a*t**2

def velocidad(v0, a, t):
    return v0+a*t
def aceleracion(a,t):
    return a

y=posicion(y0, v0, g, t)
v=velocidad(v0, g, t)
a=np.array([g]*15)
print(a)
print(y,v,a)


fig = plt.figure(figsize=(10,4))
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)
ax1.scatter(t,y)
ax2.scatter(t,v)
ax3.scatter(t,a)
plt.show()