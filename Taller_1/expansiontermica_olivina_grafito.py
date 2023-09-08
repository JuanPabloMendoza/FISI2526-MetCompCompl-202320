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
objeto = [object(fullpath), 'Grafito']
objeto2 = [object(fullpath2), 'Olivina']
objetos = [objeto, objeto2]



try:
    for objeto_ in objetos:
        promedio_coeficiente, error_global, fig = coef(objeto_[0])
        fig.savefig(f'Graficas V(T) alpha(T) {objeto_[1]}')
        print(promedio_coeficiente)
        plt.show()
except ValueError:
    print('No se tienen datos para esta temperatura')
