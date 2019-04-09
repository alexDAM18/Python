fichero = open('alumnos.txt')




def mostrarTurno7():
    fichero.readline()
    contenido = fichero.readlines()
    for linia in contenido:
        liniaSplit = linia.split(":")

        if liniaSplit[3] == "7":
            print("DNI: ", liniaSplit[0])


print("Mostar DNI de las personas del turno 7 :")
mostrarTurno7()
fichero.close()

fichero = open('alumnos.txt')
ficheroSalida = open('alumnosI.txt', 'w')

def intercambiarTurnos():
    ficheroSalida.write(fichero.readline())
    contenido = fichero.readlines()

    for linia in contenido:
        liniaSplit = linia.split(":")
        if liniaSplit[3] == "4":
            liniawrite=liniaSplit[0]+":"+liniaSplit[1]+ ":"+ liniaSplit[2]+ ":"+"8:"
            ficheroSalida.writelines(str(liniawrite)+'\n')

        else:
            if liniaSplit[3] == "8":
                liniawrite=liniaSplit[0]+":"+liniaSplit[1]+ ":"+ liniaSplit[2]+ ":"+"4:"
                ficheroSalida.write(str(liniawrite)+'\n')
            else:
                ficheroSalida.write(linia)


print("Intercambiar personas del turno 4 y 8")
intercambiarTurnos()
fichero.close()
ficheroSalida.close()
