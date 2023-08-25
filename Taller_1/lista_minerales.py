


f = open("materiales.txt", "r")
lineas = f.readlines()
f.close()
datos = []
for linea in lineas:
    datos.append(linea.strip().split(';'))
    