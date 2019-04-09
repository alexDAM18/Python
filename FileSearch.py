f = open("datos", "r")
opcion = str(input("Elige un opción: \n 1 - Población \n 2 - Edad \n 3 - Asignatura"))


f.readline()

if opcion == "1":
    pob = str(input("Introduce una población: "))
    with f as reader:
        print("Alumnos según la población")
        print("-----------------")

        for line in reader:
            splitLinea = line.split()
            if pob == splitLinea[3]:
                print("Alumno:", splitLinea[0])

        print("-----------------")

if opcion == "2":
    edad = str(input("Introduce una edad"))
    with f as reader:
        print("Alumnos y su población según la edad")
        print("---------------------------")

        for line in reader:
            splitLinea = line.split()
            if edad == splitLinea[1]:
                print("Alumno:", splitLinea[0], "| Población:", splitLinea[3])

        print("---------------------------")

if opcion == "3":
    asig = str(input("Introduce una asignatura"))
    with f as reader:
        print("Alumnos matriculados en la asignatura ", asig)
        print("---------------------------------------")

        for line in reader:
            try:
                splitLinea = line.split()
                splitAsig = splitLinea[2].split(",")
                if asig == splitAsig[0] or asig == splitAsig[1]:
                    print("Alumno:", splitLinea[0], "| Edad:", splitLinea[1], "| Procedencia:", splitLinea[3])

            except IndexError:
                print()

f.close()

with f as reader:
    try:
        for line in reader:

    except IndexError:
        print()