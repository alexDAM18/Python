fichero = open('alumnos.txt')

ficheroSalida = open('alumnosT.txt', 'w')


def asignacionTurnos():
    ficheroSalida.write(fichero.readline())

    contenido = fichero.readlines()

    for linia in contenido:
        liniaSplit = linia.split(":")

        DNI=liniaSplit[0]
        if DNI[7]!="0":
            turno = DNI[7]
        else:
            turno=10;
        liniawrite=liniaSplit[0]+":"+liniaSplit[1]+ ":"+ liniaSplit[2]+ ":"+str(turno)+":"
        ficheroSalida.write(str(liniawrite)+"\n")




print("Asignacion turnos automaticamente:")
asignacionTurnos()
fichero.close()
ficheroSalida.close()
