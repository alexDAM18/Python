f = open("alumnos", "r")
d = open("destino", "w")

datos = f.readline()

with f as reader:
    print("DNI de los alumnos del turno 7")

    for line in reader:
        splitLinea = line.split()
        if "7" == splitLinea[3]:
            print("DNI:", splitLinea[0])
        else:
            if splitLinea[3] == "4":
                splitLinea[3] = "8"
            else:
                if splitLinea[3] == "8":
                    splitLinea[3] = "4"

        newLine = splitLinea[0]+ ":"+ splitLinea[1]+ ":"+ splitLinea[2]+ ":"+ splitLinea[3]+ "\n"
        d.write(newLine)



