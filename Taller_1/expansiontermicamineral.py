import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import mineral as m
import pandas as pd

class ExpansionTermicaMineral(m.Mineral):
    def __init__(self, ruta_csv) -> None:
        df = pd.read_csv(ruta_csv, sep=',')
        df['celsius_temperature'] = df['celsius_temperature'].astype(float)
        df['volume_cc'] = df['volume_cc'].astype(float)
        self.temperatura = list(df['celsius_temperature'])
        self.volumen = list(df['volume_cc'])
    
    def coeficiente_dilatacion_termica(self):
        def derivada_central_discreta(x_i, x_f, y_i, y_f):
            #retorna derivada en xn, donde -h=x_{n-1} y h=x_{n+1}
            return (y_f-y_i)/(2*(x_f-x_i))
        temp_y_dvdT = np.zeros((len(self.temperatura), 2))
        coeficiente = np.zeros((len(self.temperatura), 2))
        for i in range(len(self.temperatura)):
            temp_y_dvdT[i][0] = self.temperatura[i]
            #
            coeficiente[i][0] = self.temperatura[i]
        for i in range(len(self.temperatura)):
            if i==0:
                temp_y_dvdT[i][1] = derivada_central_discreta(self.temperatura[i], self.temperatura[i+1], self.volumen[i], self.volumen[i+1])
                coeficiente[i][1] = (1/self.volumen[i])*temp_y_dvdT[i][1]            
            elif i==(len(self.temperatura)-1):
                temp_y_dvdT[i][1] = derivada_central_discreta(self.temperatura[i-1], self.temperatura[i], self.volumen[i-1], self.volumen[i])
                coeficiente[i][1] = (1/self.volumen[i])*temp_y_dvdT[i][1]   
            else:
                temp_y_dvdT[i][1] = derivada_central_discreta(self.temperatura[i-1], self.temperatura[i+1], self.volumen[i-1], self.volumen[i+1])
                coeficiente[i][1] = (1/self.volumen[i])*temp_y_dvdT[i][1]   
        
        suma = 0
        for i in range(len(self.temperatura)):
            suma += coeficiente[i][1]
        promedio_coeficiente = suma/len(self.temperatura)
        error_global = np.std(coeficiente[:][1])
        fig = plt.figure(figsize=(10,4))
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)
        ax1.scatter(np.array(self.temperatura), self.volumen)
        print(coeficiente[:,1])
        ax2.scatter(np.array(self.temperatura), coeficiente[:,1])
        
        return promedio_coeficiente, error_global, fig



    
    