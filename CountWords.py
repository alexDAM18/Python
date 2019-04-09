cadena = input("Introduce una cadena de texto: ")
palabra = input("Introduce una palabra: ")

checkPalabra = ''
count = 0
aux = ""

for i in cadena:
    if i != ' ':
        checkPalabra += i
        if checkPalabra == palabra:
            aux = checkPalabra
            count += 1
    else:
        if i == ' ':
            checkPalabra = ''

if count == 1:

    if aux != '':
        print("La palabra ", aux, " aparece un total de ", count, " vez")
elif count > 1:
  print("La palabra ", aux, " aparece un total de ", count, " veces")

else:
    print("Tu palabra no aparece en la cadena")





