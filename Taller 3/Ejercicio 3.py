import numpy as np
#Solo se puede encontrar el valor propio máximo o mínimo

def MaxtrixMultiplication(A,B):
    #Check dim
    a,b = A.shape
    c,d = B.shape
    if b!=c:
        return None
    n=c
    AB = np.zeros(shape=(a,d))
    for i in range(a):
        for j in range(d):
            for k in range(n):
                AB[i,j] += A[i,k]*B[k,j]
    return AB

z = np.matrix([[1],[0],[0]], dtype='float64')

def RayleighQuotient(A,v):
    return (MaxtrixMultiplication(v.T, MaxtrixMultiplication(A,v)))/(MaxtrixMultiplication(v.T, v))

def MaxEigenValue(A, z, tolerancia=1e-7, itmax=1000):
    Normalized = (1/np.linalg.norm(z))*z
    EValue = 0
    Error = np.linalg.norm(MaxtrixMultiplication(A,Normalized) - EValue*Normalized)
    it=0
    while Error>tolerancia and itmax>it:
        z = MaxtrixMultiplication(A,Normalized)
        Normalized = (1/np.linalg.norm(z))*z
        EValue = RayleighQuotient(A,Normalized)
        Error = np.linalg.norm(MaxtrixMultiplication(A,Normalized) - EValue*Normalized)
        it+=1
    return EValue[0,0], Normalized

def MinEigenValue(A, z, tolerancia=1e-7, itmax=1000):
    A = np.linalg.inv(A)
    Normalized = (1/np.linalg.norm(z))*z
    EValue = 0
    Error = np.linalg.norm(MaxtrixMultiplication(A,Normalized) - EValue*Normalized)
    it=0
    while Error>tolerancia and itmax>it:
        z = MaxtrixMultiplication(A,Normalized)
        Normalized = (1/np.linalg.norm(z))*z
        EValue = RayleighQuotient(A,Normalized)
        Error = np.linalg.norm(MaxtrixMultiplication(A,Normalized) - EValue*Normalized)
        it+=1
    return (1/EValue)[0,0], Normalized



m1 = 1
m2 = 1
m3 = 1
k11 = -2
k12 = 1
k13 = 0
k21 = 1
k22 = -2
k23 = 1
k31 = 0
k32 = 1
k33 = -2

print(f'Tomemos\nm1 = {m1}, m2 = {m2}, m3 = {m3},\nk11 = {k11},k12 = {k12}, k13 = {k13},\nk21 = {k21}, k22 = {k22}, k23 = {k23},\nk31 = {k31}, k32 = {k32}, k33 = {k33}')
A = np.array([[k11/m1,k12/m2,k13/m3],[k21/m1,k22/m2,k23/m3],[k31/m1,k32/m2,k33/m3]], dtype='float64')
max_fr, max_amp = MaxEigenValue(A,z)
min_fr, min_amp = MinEigenValue(A,z)

print(f'{max_fr}\n{min_fr}\n{max_amp}\n{min_amp}')

        