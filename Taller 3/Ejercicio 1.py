import numpy as np

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

#a
Aa = np.array([[5,-4,-2],[5,-5,4],[2,5,-4],[-5,4,3],[3,-4,-3]], dtype='float64')
Ba = np.array([[5],[-2],[-3]], dtype='float64')
print(MaxtrixMultiplication(Aa,Ba))

#b
Ab = np.array([[0,-1,-1,3],[5,-5,-2,2],[1,0,4,5]], dtype='float64')
Bb = np.array([[0,-3],[-2,-1],[3,-3]], dtype='float64')
print(MaxtrixMultiplication(Ab,Bb))

#c
Ac = np.array([[2,-5,5,1],[5,2,-7,-6],[-6,-1,7,-4],[5,4,1,-5]], dtype='float64')
Bc = np.array([[0,4,-7,1,-6],[-1,-6,-5,1,1],[2,-1,-6,5,-5],[-3,-6,6,3,5]])
print(MaxtrixMultiplication(Ac,Bc))


Bcc = Bc[:,:4]
print(Bcc)
print(f'Observe que en el ejemplo C, siendo A la primera matriz y B la segunda\n sin la ultima columna vemos que AB es \n{MaxtrixMultiplication(Ac,Bcc)}\n pero BA es \n{MaxtrixMultiplication(Bcc,Ac)}')