import mineral as m
import expansiontermicamineral as exptermin
import os
import matplotlib.pyplot as plt

def object(archivo_csv):
    objeto =  exptermin.ExpansionTermicaMineral(archivo_csv)
    return objeto

def coef(object):
    return object.coeficiente_dilatacion_termica()

fullpath = os.path.abspath('Taller_1/graphite_mceligot_2016.csv')
fullpath2 = os.path.abspath('Taller_1/olivine_angel_2017.csv')
objeto = object(fullpath)



try:
    promedio_coeficiente, error_global, fig = coef(objeto)
    print(promedio_coeficiente)
    plt.show()
except ValueError:
    print('No se tienen datos para esta temperatura')
