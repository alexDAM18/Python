archivo = input("Introduce un archivo para modificar: ")
archivo_new = open("ArchivoMayus.txt", "w")

f = open(archivo, "r")
leer = f.read().upper()
f_mayus = archivo_new.write(leer)
f.close()
