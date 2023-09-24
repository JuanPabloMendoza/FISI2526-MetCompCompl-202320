import numpy as np
import matplotlib.pyplot as plt

def Integral_MonterCarlo(funcion, a,b, N):
    x = np.random.uniform(a,b,N)
    fi = funcion(x)
    return (b-a)*sum(fi)/N

def funcion_integrar(x):
    return np.exp(-x)*np.sin(x)  

I = Integral_MonterCarlo(funcion_integrar, 0, np.pi, 10000)
I_real = 0.5*(1+np.exp(-np.pi))
error = 100-(100*I/I_real)
print(f'I = {I}, I_real = {I_real}, Error = {error}')

def Montecarlo_N(N_min, N_max, salto):
    rango_n = np.array(list(range(N_min, N_max+1, salto)), dtype='int64')
    Error= np.array([])
    for n in rango_n:
        I = Integral_MonterCarlo(funcion_integrar, 0, np.pi, n)
        I_real = 0.5*(1+np.exp(-np.pi))
        error = np.abs(100-(100*I/I_real))
        Error = np.append(Error, error)
        #print(f'I = {I}, I_real = {I_real}, Error = {error}', n)
    return rango_n, Error


N, Error = Montecarlo_N(10000, 10**6, 10000)
cota = 100/np.sqrt(N)
plt.plot(N, cota, label = 'cota')
plt.scatter(N, Error, color = 'red', label = 'error')
plt.legend()
plt.show()



#Ejercicio 3
def Integral_MonterCarlo_esfera(funcion, N):
    a=-1
    b=1
    x = np.random.uniform(a,b,N)
    y = np.random.uniform(a,b,N)
    z = np.random.uniform(a,b,N)
    suma = 0
    for i in range(N):
        if x[i]**2+y[i]**2+z[i]**2<=1:
            suma += funcion(x[i],y[i],z[i]) #Se suma uno puesto que la función es 1
    return 8*suma/N

def funcion(x,y,z):
    return np.sin((x**2)+(y**2)+(z**2))*np.exp((x**2)+(y**2)+(z**2))

I = Integral_MonterCarlo_esfera(funcion, 10000000)
print(I)

