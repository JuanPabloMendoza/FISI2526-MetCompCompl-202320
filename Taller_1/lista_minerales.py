import pandas as pd
import mineral as m

df = pd.read_table('/Users/juanpablomendozaarias/Library/Mobile Documents/com~apple~CloudDocs/Universidad/Tercer Semestre/Métodos Computacionales/MetCompCompl-202320 {MENDOZA} {LIÉVANO}./Taller_1/minerales.txt', sep='\t', encoding_errors='ignore')
lista_minerales = []
def crear_minerales(dato, lista_minerales):
    nombre = row[1]
    dureza = row[2]
    rompimiento_por_fractura = row[3]
    color = row[4]
    composicion = row[5]
    lustre = row[6]
    specific_gravity = row[7]
    sistema_cristalino = row[8]
    mineral = m.Mineral(nombre, dureza, lustre, rompimiento_por_fractura, color, composicion, sistema_cristalino, specific_gravity)
    lista_minerales.append(mineral)
for row in df.itertuples():
    crear_minerales(row, lista_minerales)


def numero_silicatos(minerales):
    cont = 0
    for mineral in minerales:
        if mineral.silicato():
            cont+=1
    return cont

def promedio_densidad(minerales):
    suma = 0
    for mineral in minerales:
        suma += mineral.densidad()
    return suma/len(minerales)

""" 

for mineral in lista_minerales:
    attrs = vars(mineral)
    mineral.color_()
    print(', '.join("%s: %s" % item for item in attrs.items()))
    
print(numero_silicatos(lista_minerales))
print(promedio_densidad(lista_minerales))

mineral = lista_minerales[1]
mineral.color_()
 """

