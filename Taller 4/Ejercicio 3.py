import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

#1
def f(x):
    if x>= -1. and x<= 2.:
        return (1/3)*x**2
    else:
        return 0

#a
Norm = integrate.quad(f,-np.inf,np.inf, full_output=1)[0]
ProbA = integrate.quad(f,0,1., full_output=1)[0]/Norm
ProbB = integrate.quad(f,1,2., full_output=1)[0]/Norm
print(f'\nP(0<X<=1) = {np.round(ProbA,3)}')
print(f'P(1<X<=2) = {np.round(ProbB,3)}\n')

#2
mu = 78
Var = 36
sigma = np.sqrt(Var)
def Normal(x,mu=mu,sigma=sigma):
    return 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2) )

#a
ProbA = integrate.quad(Normal, 72, np.inf)[0]
print(f'La probabilidad de que una persona que haga el examen alcance calificaciones mayores de 72 es de {np.round(ProbA,3)}\n')
#b 
N = int(1e4)
X = np.linspace(0,100,N)
lim = 0.1
i=1
I = integrate.quad(Normal, X[0], np.inf)[0]
while (i<N and I>lim):
    I = integrate.quad(Normal, X[i], np.inf)[0]
    i+=1

print(f'La calificación mínima que un estudiante debe recibir para ganar una calificación de A es {np.round(X[i],3)}\n')
#c
N = int(1e4)
X = np.linspace(0,100,N)
lim = 0.281
i=1
I = integrate.quad(Normal, X[0], np.inf)[0]
while (i<N and I>lim):
    I = integrate.quad(Normal, X[i], np.inf)[0]
    i+=1
c = X[i]
print(f'El punto límite para pasar el examen si el examinador desea pasar a sólo 28,1% más alto de todas las calificaciones es {np.round(c,3)}\n')
#d
N = int(1e4)
X = np.linspace(0,100,N)
lim = 0.25
I=0
i=0
while (i<N and I<lim):
    I = integrate.quad(Normal, -np.inf, X[i])[0]
    i+=1
ProporcionD = integrate.quad(Normal, X[i]+5, np.inf)[0]
print(f'Aproximadamente, el {np.round(ProporcionD,3)*100}% de estudiantes tienen 5 o más puntos arriba de la calificación que corta al 25% más bajo\n')

#e
#aplicamos bayes: P((>84)|(>72)) = P((>84)int(>72))/P(>72) = P(>84)/P(>72)
ProbE = integrate.quad(Normal, 84, np.inf)[0]/integrate.quad(Normal, 72, np.inf)[0]
print(f'La probabilidad de que su calificación exceda de 84 dado que se sabe que excede de 72 es {np.round(ProbE,3)}')