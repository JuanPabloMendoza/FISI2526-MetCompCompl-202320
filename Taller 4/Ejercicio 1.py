import numpy as np
import matplotlib.pyplot as plt

""" Baraja = list(range(1,53))
N=int(1e7)

def GetSample(Events, N = int(1e5), ncartas = 5, Weights = None):
    Sample = np.zeros((N,ncartas))
    
    for i in range(N):
        
        if Weights == None:
            Exp = np.random.choice(Events, ncartas, replace=False)
        
        Sample[i] = Exp
    return Sample

def ExcluirEnBaraja(Baraja, Posibles, N):
    i=0
    while i<N:
        ElementoAExcluir = np.random.choice(Posibles, 1, replace=False)[0]
        Baraja = np.delete(Baraja, np.where(Baraja == ElementoAExcluir))
        Posibles = np.delete(Posibles, np.where(Posibles == ElementoAExcluir))
        i+=1
    return Baraja
      

#1
print(f'1:')
#a
BarajaInicial = np.copy(Baraja)
Espadas = np.copy(BarajaInicial[0:13])
N_EspadasIniciales = 2
BarajaInicial = ExcluirEnBaraja(BarajaInicial, Espadas, N_EspadasIniciales)

Sample = GetSample(BarajaInicial, N, ncartas=3)
frecuencia=0

for i in range(Sample.shape[0]):
    nespadas = 0
    for j in range(Sample.shape[1]):
        if Sample[i,j] <= 13:
            nespadas +=1
    if nespadas==3:
        frecuencia +=1

Prob1 = frecuencia/N
print(f'a: Si las primeras 2 cartas son espadas, la probabilidad de que las siguientes 3 cartas también sean espadas es de {Prob1}')


#b
BarajaInicial = np.copy(Baraja)
Espadas = np.copy(BarajaInicial[0:13])
N_EspadasIniciales = 3
BarajaInicial = ExcluirEnBaraja(BarajaInicial, Espadas, N_EspadasIniciales)

Sample = GetSample(BarajaInicial, N, ncartas=2)
frecuencia=0

for i in range(Sample.shape[0]):
    nespadas = 0
    for j in range(Sample.shape[1]):
        if Sample[i,j] <= 13:
            nespadas +=1
    if nespadas==2:
        frecuencia +=1

Prob2 = frecuencia/N
print(f'b: Si las primeras 3 cartas son espadas, la probabilidad de que las siguientes 2 cartas también sean espadas es de {Prob2}')

#c
BarajaInicial = np.copy(Baraja)
Espadas = np.copy(BarajaInicial[0:13])
N_EspadasIniciales = 4
BarajaInicial = ExcluirEnBaraja(BarajaInicial, Espadas, N_EspadasIniciales)

Sample = GetSample(BarajaInicial, N, ncartas=1)
frecuencia=0

for i in range(Sample.shape[0]):
    nespadas = 0
    for j in range(Sample.shape[1]):
        if Sample[i,j] <= 13:
            nespadas +=1
    if nespadas==1:
        frecuencia +=1

Prob3 = frecuencia/N
print(f'c: Si las primeras 4 cartas son espadas, la probabilidad de que la siguiente carta también sea espada es de {Prob3}')
 """
#2
N = int(1e6)
ProbGripe = 0.6

ProbVacuna = np.random.randint(0,N)/N
ProbGripaSinVacuna = 0.9
ProbNoGripaConVacuna = 0.8
ProbGripaConVacuna = 1-ProbNoGripaConVacuna

PersonasConGripe = np.array([[1,0]]*N*ProbGripe)
PersonasSinGripe = np.array([[0,0]]*(N-N*ProbGripe))

PersonasConGripe[:int(PersonasConGripe*ProbGripaConVacuna),1] = 1





