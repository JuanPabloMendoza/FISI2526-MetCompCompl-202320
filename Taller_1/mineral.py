import matplotlib.pyplot as plt
import matplotlib
import numpy as np

class EventoSismico:
    def __init__(self, horaLocal: str, magnitud: float, lugar: str, agencia:str):
        self.horaLocal = horaLocal
        self.magnitud = float(magnitud)
        self.lugar = lugar
        self.agencia = agencia

    def municipio(self):
        return self.lugar.split('-')[0].strip()
    
    def departamento(self) -> str:
        return self.lugar.split('-')[1].split(',')[0].strip()
    
    def pais(self) -> str:
        return self.lugar.split(',')[1].strip()

    def agencia_SGC(self) -> bool:
        return self.agencia == 'SGC'
    
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
        if 'Si' in self.composicion or 'O' in self.composicion:
            return True
    
    def densidad(self):
        return self.specific_gravity*997
    
    def color(self):
        rgb = matplotlib.colors.to_rgb(self.color)
        array = np.array([rgb[0], rgb[1], rgb[2]])
        plt.imshow(array)
        plt.show()
    
    def dureza(self):
        print(self.dureza)
        
    def rompimiento(self):
        print(self.rompimiento_por_fractura)
        
    def organizacion(self):
        print(self.sistema_cristalino)
        
rgb = matplotlib.colors.to_rgb('#F56FFF')
rgb_ = []
for cod in rgb:
    rgb_.append(cod*256)
print(rgb_)
array = np.array(rgb_)
plt.imshow([rgb_], )
plt.show()
                
