import numpy as np

TR = np.array([[0.4,0.2,0.2,0.2],
              [0.25,0.25,0.25,0.25],
              [0.3,0.3,0.1,0.3],
              [0.1,0.1,0.1,0.7]]).T

P = np.array([0.25,0.,0.5,0.25])

#1
A = 0
C = 1
G = 2
T = 3

GenDeseado = 'T,G,C,T,C,A,A,A'
Deseado = np.array([T,G,C,T,C,A,A,A])

Prob = 1
Anterior = P
Prob = Anterior[Deseado[0]]

for i in range(1,Deseado.size):
    Prob *= TR[Deseado[i],Deseado[i-1]]
print(f'La probabilidad de obtener el gen {GenDeseado} es {Prob}')

#2
A = 3
C = 2
G = 1
U = 0
E = np.array([[0.8,0.05,0.5,0.1],
              [0.,0.9,0.1,0.],
              [0.,0.1,0.9,0.],
              [0.2,0.1,0.,0.7]])

GenTraducido = 'A,C,G,A,G,U,U,U'
Observado = np.array([A,C,G,A,G,U,U,U])
for i in range(Observado.size):
    Prob *= E[Observado[i],Deseado[i]]
print(Prob)
print(f'La probabilidad de que el gen traducido {GenTraducido} provenga del gen {GenDeseado} es {Prob}')


