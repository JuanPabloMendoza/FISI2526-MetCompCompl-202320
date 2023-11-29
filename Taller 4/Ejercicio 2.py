import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


#1
def Binomial(n,p,a, N=int(1e4)):
    Evento = np.random.binomial(n,p,N)
    Pedido = Evento[Evento<=a]
    return Pedido.size/N

def GraphBin(Caso,N):
    P = np.linspace(0,1,N)
    for caso in Caso: 
        Probabilidad = np.empty((N))
        for i in range(N):
            Probabilidad[i] = Binomial(caso[0],P[i],caso[1])
        plt.plot(P,Probabilidad, label=f'N={caso[0]}, a={caso[1]}')
    plt.ylabel('Probabilidad de aceptación')
    plt.xlabel('p')
    plt.legend()
    plt.show()

Caso1 = [5,1]
Caso2 = [25,5]
N =int(1e3)
Caso = np.array([Caso1,Caso2])
GraphBin(Caso,N)

#a
a = 0
b = 0.1
f1 = lambda x: Binomial(Caso1[0],x,Caso1[1])

Plan1 = integrate.quad(f1,a,b, full_output=1)[0]/integrate.quad(f1,0,1, full_output=1)[0]
print(f'Primer plan: {Plan1}')

f2 = lambda x: Binomial(Caso2[0],x,Caso2[1])
Plan2 = integrate.quad(f2,a,b, full_output=1)[0]/integrate.quad(f2,0,1, full_output=1)[0]
print(f'Segundo plan: {Plan2}')
if Plan1>Plan2:
    print(f'Es mejor opción el plan 1')
else:
    print(f'Es mejor opción el plan 2')

#b

a = 0
b = 0.3

Plan1 = Binomial(Caso1[0],0.3,Caso1[1])
Plan2 = Binomial(Caso2[0],0.3,Caso2[1])
print(f'\nPrimer plan: {Plan1}')
print(f'Segundo plan: {Plan2}')
if Plan1<Plan2:
    print(f'Es mejor opción el plan 1')
else:
    print(f'Es mejor opción el plan 2')
    
    
""" f1 = lambda x: Binomial(Caso1[0],x,Caso1[1])
Plan1 = integrate.quad(f1,a,b, full_output=1)[0]/integrate.quad(f1,0,1, full_output=1)[0]
print(f'Primer plan: {Plan1}')

f2 = lambda x: Binomial(Caso2[0],x,Caso2[1])
Plan2 = integrate.quad(f2,a,b, full_output=1)[0]/integrate.quad(f2,0,1, full_output=1)[0]
print(f'Segundo plan: {Plan2}')
if Plan1<Plan2:
    print(f'Es mejor opción el plan 1')
else:
    print(f'Es mejor opción el plan 2')
 """

#2
def Poisson1(lam,a,N=int(1e4)):
    Eventos = np.random.poisson(lam,N)
    Pedido = Eventos[Eventos==a]
    return Pedido.size/N

def Poisson2(lam,a,N = int(1e4)):
    Eventos = np.random.poisson(lam,N)
    Pedido = Eventos[Eventos>=a]
    return Pedido.size/N

lam = 1

#a
N=50
lim = 0.01
for i in range(N):
    Prob = Poisson2(lam, i)
    if Prob<lim:
        break
print(f'El menor valor de n tal que la probabilidad de que haya al menos n desconexiones en menos de un período de 4 horas es menor que {lim} es {i}')

#b
f = lambda h: Poisson1(lam,0)**(h/4)
H = 50
for i in range(H):
    if f(i)<0.02:
        break
print(f'El menor valor del número de horas h tal que la probabilidad de que no haya desconexiones en h horas sea menor que 0.02 es de {i}')

#c
ProbDesconexionPeriodo = Poisson2(lam,0)
ProbNoDesconexionPeriodo = Poisson1(lam,0)
Prob = (ProbNoDesconexionPeriodo*ProbDesconexionPeriodo**2)*3

print(f'La probabilidad de que en 3 períodos consecutivos de 4 horas, haya solamente un período de 4 horas sin desconexiones es de {Prob}.')


#d
N=50
VEsperado = 3*lam
PVesperado = Poisson1(VEsperado, VEsperado)
print(f'La probabilidad de que el número de desconexiones en 3 períodos consecutivos de 4 horas sea igual al número esperado de desconexiones en 3 períodos consecutivos de 4 horas es de {PVesperado}')
    