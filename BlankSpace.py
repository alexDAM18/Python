"""3. Realiza un programa que lea una cadena y nos diga cuantos espacios en blanco contiene.
No podeis utilizar funciones de string"""

frase = input("Introduce una cadena de texto: ")

cuenta = 0

for space in frase:
    if space == ' ':
        cuenta+=1
print(cuenta)