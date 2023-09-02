import matplotlib.pyplot as plt
import matplotlib
import numpy as np
    
class Mineral:
    def __init__(self, nombre: str, dureza: float, lustre: str, rompimiento_por_fractura: bool, color: str, composicion: str, sistema_cristalino: str, specific_gravity: float) -> None:
        self.nombre = nombre
        self.dureza = float(dureza)
        self.lustre = lustre
        self.rompimiento_por_fractura = bool(rompimiento_por_fractura)
        self.color = color
        self.composicion = composicion
        self.sistema_cristalino = sistema_cristalino
        self.specific_gravity = float(specific_gravity)
        
    def silicato(self):
        if 'Si' in self.composicion and 'O' in self.composicion:
            return True
    
    def densidad(self):
        return self.specific_gravity*997
    
    def color_(self):
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        rect = matplotlib.patches.Rectangle((-10,-10), 20, 20, color=self.color)
        ax.add_patch(rect)
        plt.xlim([-20, 20])
        plt.ylim([-20, 20])
        plt.show()
    
    def dureza_(self):
        print(self.dureza)
        
    def rompimiento(self):
        print(self.rompimiento_por_fractura)
        
    def organizacion(self):
        print(self.sistema_cristalino)
        

                
