import numpy as np
import matplotlib.pyplot as plt


#DATOS PROBLEMA
r =12.5
B_0 = 0.05
f = 7
omega = 3.5
R = 1750

#FUNCIONES
def flujo_magnetico(t, r=r, B_0=B_0, f=f, omega=omega):
    return np.pi * (r**2) * B_0 * np.cos(omega * t) * np.cos(2 * np.pi * f * t)

#METODO DERIVADA
h = 0.00000001
def derivada_central(funcion, x,h):
    return (funcion( x + h ) - funcion( x - h ))/(2 * h)

#CONJUNTO SOPORTE
Intervalo_tiempo = [0,3]
N = 100000
X = np.linspace(Intervalo_tiempo[0], Intervalo_tiempo[1], N)
Y = flujo_magnetico(X)
I = (-1/R)*derivada_central(flujo_magnetico, X, h)

#GRÁFICA
plt.plot(X, I, color = 'black', label = 'Corriente inducida')
plt.legend()
plt.show()

#NEWTON-RAPHSON
def GetNewtonMethod(f,df,xn,itmax=100000,precision=1e-5):
    
    error = 1.
    it=0
    
    while error > precision and it<itmax:
        try:
            xn1 = xn - f(xn)/df(f,xn,h)
            error = np.abs(f(xn)/df(f,xn,h))
        except ZeroDivisionError:
            print('Division por cero')
        xn=xn1
        it+=1
    return xn



""" def roots_each_x(X, newtonmethod, f, df, err, n_raices):
    roots = []
    real_roots = []
    centinela = True
    while centinela: 
        if len(real_roots)<=n_raices:
            for x in X:
                root = newtonmethod(f, df, x)
                roots.append(root)
            
            root_i = roots[0]
            real_roots.append(root_i)
            for root in roots[1:]:
                difference = root_i-root
                if not np.abs(difference)<err:
                    real_roots.append(root_i)
                root_i= root
        else:
            centinela = False
    i=0        
    for y in df:
        if np.abs(y)<err and X[i]>start:
            real_roots.append(X[i])
    return real_roots """

def roots_each_x(X, start, f, erry, errx, n_raices):
    ###Esta tomando el primer dato que cumple la condicion para cada raiz<
    #Arreglar para que tome el mas central
    roots = []
    real_roots = []
    i=0        
    for y in f:
        if np.abs(y)<erry and X[i]>=start:
            roots.append(X[i])
        i+=1
    root_i = roots[0]
    real_roots.append(root_i)    
    for root in roots[1:]:
        difference = root_i-root
        if (not np.abs(difference)<errx) and len(real_roots)<n_raices and (root_i not in real_roots):
            real_roots.append(root)
        root_i= root
    return real_roots


#RAICES
raices = roots_each_x(X, 0, I, 0.005, 0.01, 3)
print(raices)
