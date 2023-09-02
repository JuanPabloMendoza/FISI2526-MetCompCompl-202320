import numpy as np
import matplotlib.pyplot as plt

def posicion_mas(a, w, valor_x):
    return a*np.sin(w*valor_x)

def posicion_mas__(a_,w_):
    def posicion_mas(valor_x, a=a_, w=w_):
        return a*np.sin(w*valor_x)
    return posicion_mas

def velocidad_mas__(a_,w_):
    def velocidad_mas(valor_x, a=a_, w=w_):
        return a*np.cos(w*valor_x)
    return velocidad_mas

def velocidad_mas(a, w, valor_x):
    return a*w*np.cos(w*valor_x)
    

def punto_medio(xi,xf):
    return (xi+xf)/2

def signo(funcion, x):
    return funcion(valor_x=x)/np.abs(funcion(valor_x=x))
    
def metodo_biseccion(funcion,xi,xf, cero=0, i=1):
    a=xi
    b=xf
    c = punto_medio(xi ,xf)
    if funcion(valor_x=c)==0:
        return (c, funcion(valor_x=c))
    elif i<100 and funcion(valor_x=c)!=0:
        if signo(funcion,a)*signo(funcion,c)==-1:
            return metodo_biseccion(funcion, a,c,c, i+1)
        elif signo(funcion,c)*signo(funcion,b)==-1:
            return metodo_biseccion(funcion, c,b, c, i+1)
    else:
        return (c, funcion(valor_x=c))

""" def recta(valor_x):
    return 2*valor_x+2
 """
 
def derivada_central(funcion, x, h):
    derivada_x = ((funcion(x+h)-funcion(x-h))/(2*h))
    return derivada_x

def derivada_derecha(funcion, x, h):
    derivada_x = ((funcion(x+h)-funcion(x))/(h))
    return derivada_x

def derivada_izquierda(funcion, x, h):
    derivada_x = ((funcion(x)-funcion(x-h))/(h))
    return derivada_x
        