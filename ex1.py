import unicodedata
fichero = open('notas.txt')
ficheroAprobados= open('aprobados.txt', 'w')
ficheroSuspendidos= open('suspendidos.txt', 'w')
ficheroAlumnos=open('alumnos.txt', 'w')



def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',cadena) if unicodedata.category(c) != 'Mn'))
    return s

fichero.readline()
contenido = fichero.readlines()
media=0
for linia in contenido:
    liniaSplit = linia.split(":")
    media=(int(liniaSplit[2])+int(liniaSplit[3])+int(liniaSplit[4])+int(liniaSplit[5]))/4
    nombre = str(liniaSplit[1] + " " + liniaSplit[0])
    nombre2=elimina_tildes(nombre)
    #nombre2 = unicodedata.normalize("NFKD", str(nombre))
    #nombre2 = nombre2.encode("utf8").decode("ascii", "ignore")
    print(nombre2)
    lineaSalidaAlumno=nombre2+".txt"
    if media>=5:
        ficheroAprobados.write(nombre+"\n")
        frase = nombre + " ha obtenido una media de " + str(media) + " la cual le permite superar el modulo"


    else:
        ficheroSuspendidos.write(nombre+"\n")
        frase = nombre + " ha obtenido una media de " + str(media) + " la cual no le permite superar el modulo"

    ficheroSalida = open(lineaSalidaAlumno, 'w')
    ficheroSalida.write(frase + "\n")
    ficheroSalida.close()
    ficheroAlumnos.write(frase+"\n")


fichero.close()
ficheroAlumnos.close()
ficheroSuspendidos.close()
ficheroAprobados.close()