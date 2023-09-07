import numpy as np
import matplotlib.pyplot as plt
import os
import glob

def Data(archivo):
    arreglo_tuplas = []
    datos = open(archivo, 'r')
    lineas = datos.readlines()
    index_empezar = lineas.index('    data: |\n')+1
    for i in range(index_empezar, len(lineas)):
        try:
            linea = lineas[i].strip()
            if linea != "": 
                lista = linea.split(" ")
                tupla = (float(lista[0]), float(lista[1]))
                arreglo_tuplas.append(tupla)
        except:
            break
    nparray = np.array(arreglo_tuplas, dtype=[('Longitud_onda', float), ('Indice_refraccion', float)])
    datos.close()
    return nparray
            
print(Data("Taller_1/Adhesivos Ópticos/NOA1348.yml"))

def Grafico(archivo):
    nparray = Data(archivo)
    nombre_material = os.path.splitext(os.path.basename(archivo))[0]
    X = np.empty(nparray.size)
    Y = np.empty(nparray.size)
    
    for i in range(nparray.size):
        X[i] = nparray[i][0]
        Y[i] = nparray[i][1]

    n = np.round(np.mean(Y), 5)
    desviacion_est = round(np.std(Y), 5)
    

    fig,axs = plt.subplots(figsize=(6,5))
    axs.scatter(X,Y,s=8)
    axs.set_ylabel('Índice de Refración')
    axs.set_xlabel('Longitud de Onda (nm)')
    axs.set_title(f'{nombre_material}\n n Promedio: {n} - Desviación Estandar: {desviacion_est}')
    fig.savefig(archivo.replace(".yml",".png"))
    return axs

Kaptonruta= "Taller_1/Plásticos Comerciales/Kapton.yml"
NOA1348ruta="Taller_1/Adhesivos Ópticos/NOA1348.yml"

""" Grafico(Kaptonruta)
plt.show()
Grafico(NOA1348ruta)
plt.show() """

def Graficas_generalizadas():
    categorias = [x[0] for x in os.walk('Taller_1')]
    if 'Taller_1' in categorias:
        categorias.remove('Taller_1')
    if 'Taller_1/__pycache__' in categorias:
        categorias.remove('Taller_1/__pycache__')
    
    for i in range(len(categorias)):
        rutas=glob.glob(f'{categorias[i]}/*.yml', recursive=True)
        for i in rutas:
            Grafico(i)
            plt.close()
            
Graficas_generalizadas()