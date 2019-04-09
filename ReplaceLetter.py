cadena = input("Introduce una cadena de texto: ")
letra = input("Introduce una letra para sustituir: ")
result = ''

for i in cadena:
        if i == letra:
                i = '_'
        result += i
print (result)






