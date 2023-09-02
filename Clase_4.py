import numpy as np
import matplotlib.pyplot as plt
import funciones as f


N=100
A=2
k=800
m=2
w=np.sqrt(k/m)
t=np.linspace(0,0.2,N)
posicion = f.posicion_mas(A,w,t)
velocidad = f.velocidad_mas(A,w,t)
velocidad_izquierda = f.derivada_izquierda(f.posicion_mas__(A, w), t, 0.001)
velocidad_derecha = f.derivada_derecha(f.posicion_mas__(A, w), t, 0.001)
velocidad_central = f.derivada_central(f.posicion_mas__(A, w), t, 0.001)
cero,cero_ = f.metodo_biseccion(f.velocidad_mas__(A, w), 0, 0.1)


fig = plt.figure(figsize=(20,8))
ax = plt.scatter(t, velocidad, label='Exacta')
ax2 = plt.scatter(t, velocidad_izquierda, label='Izquierda')
ax3 = plt.scatter(t, velocidad_derecha, label='Derecha')
ax4 = plt.scatter(t, velocidad_central, label='Central')
plt.legend()
plt.show()