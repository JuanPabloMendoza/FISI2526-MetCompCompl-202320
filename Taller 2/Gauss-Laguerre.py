import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)
#Cantidades estandar
N_a = 6.0225*(10**23)
k = 1.3805*(10**(-23))

#GAUSS-LAGUERRE
def GetLaguerreRecursive(n,x):

    if n==0:
        poly = sym.Pow(1,1)
    elif n==1:
        poly = 1-x
    else:
        poly = ((2*n-1-x)*GetLaguerreRecursive(n-1,x)-(n-1)*GetLaguerreRecursive(n-2,x))/n
   
    return sym.simplify(poly)

print(GetLaguerreRecursive(5,x))

#RAICES

def GetDLaguerre(n,x):
    Pn = GetLaguerreRecursive(n,x)
    return sym.diff(Pn,x,1)

def GetNewton(f,df,xn,itmax=10000,precision=1e-10):
    ##revisar precision ######
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
            error = np.abs(f(xn)/df(xn))
            
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn
    
def GetRootsGLag(f,df,x,tolerancia = 11):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)
        croot = np.round( root, tolerancia )
        
        if croot not in Roots:
            Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots

def GetAllRootsGLag(n):
    a = 0
    b = n+(n-1)*np.sqrt(n)
    xn = np.linspace(a,b,100)
    
    Laguerre = []
    DLaguerre = []
    
    for i in range(n+1):
        Laguerre.append(GetLaguerreRecursive(i,x))
        DLaguerre.append(GetDLaguerre(i,x))
    
    poly = sym.lambdify([x],Laguerre[n],'numpy')
    Dpoly = sym.lambdify([x],DLaguerre[n],'numpy')
    Roots = GetRootsGLag(poly,Dpoly,xn)
    
    return Roots

print(GetAllRootsGLag(4))

def GetWeightsGLag(n):

    Roots = GetAllRootsGLag(n)

    

    Laguerre = []
    
    for i in range(n+2):
        Laguerre.append(GetLaguerreRecursive(i,x))
    
    poly = sym.lambdify([x],Laguerre[n+1],'numpy')
    Weights = []
    for root in Roots:
        Weights.append(root/(((n+1)**2)*(poly(root))**2))
    
    return Weights

print(GetWeightsGLag(4))

#INTEGRAL 0 A INF

def Integral_GL(funcion, n):
    def funcion_corregida(x):
        return funcion(x) * np.exp(x)
    raices = GetAllRootsGLag(n)
    pesos = GetWeightsGLag(n)
    suma = 0
    for i in range(n):
        suma += pesos[i] * funcion_corregida(raices[i])
    return suma


def Integral_GL_corta(funcion, n):
    def funcion_corregida(x):
        return funcion(x) * np.exp(x)
    n = 80
    raices,pesos = np.polynomial.laguerre.laggauss(n)
    suma = 0
    for i in range(n):
        suma += pesos[i] * funcion_corregida(raices[i])
    return suma

#EJEMPLO
def funcion(x):
    return np.exp(-x)*np.cos(x)

#print(Integral_GL_corta(funcion, 10))

#EJERCICIOS PRACTICOS

#2

def P(v, T=300, m=0.001, R=k):
    M = m/N_a
    return 4 * np.pi * (( M / ( 2 * np.pi * R * T ))**(3/2)) * (v**2) * np.exp(-(M * (v**2))/( 2 * R * T))

v = np.linspace(0, 1000, 10000)
temperaturas = np.array([50, 100, 189.15, 300, 500, 600, 1000, 2500, 5000, 10000], dtype='float64')
masa_helio = 0.004
masa_nitrogeno = 0.028

""" for temp in temperaturas:
    plt.plot(v, P(v, temp, masa_helio), label = f'T = {temp} K')
plt.legend()
plt.show() """

plt.plot(v, P(v, 298.15, masa_helio), label = f'T = {298.15} K')
plt.legend()
plt.show()


def velocidad_promedio(m, T):
    def v_pv(v):
        return v*P(v, T, m)
    velocidad_promedio = Integral_GL(v_pv, 10)
    return velocidad_promedio

def velocidad_promedio_real(m, T):
    M = m/N_a
    return np.sqrt((8*k*T)/((np.pi)*M))

print(velocidad_promedio(masa_nitrogeno, 300))
print(velocidad_promedio_real(masa_nitrogeno, 300))


print(f'R2: A medida que aumenta la temperatura se puede observar que la velocidad más frecuente o probable aumenta también.')
print(f'Esto puede deducirse de la ecuacion de velocidad promedio, la cual tiene una relacion creciente con la temperatura')
print(f'También, dado que la temperatura es una medida de la energía cinética del sistema. Por esto, a medida que la temperatura aumenta, la energía cinética también, por lo que la velocidad promedio de las partículas se incrementa.')


#3
temperaturas = np.array([50, 100, 200, 300, 500, 700, 1000, 2500, 5000, 10000], dtype='float64')
velocidad_promedio = np.array([])

""" for temperatura in temperaturas:
    def v_pv(v):
        return P(v, temperatura)
    velocidad_promedio = np.append(velocidad_promedio, Integral_GL(v_pv, 5))
print(velocidad_promedio) """
    






        