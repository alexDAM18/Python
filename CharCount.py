"""4. Realiza un programa que lea una cadena y nos diga cuantas palabras contiene. No podeis
utilizar funciones de string."""

frase = input("Introduce una cadena de texto: ")

cuenta = 0

for i in range(1, len(frase)):
    if frase[i] == ' ' and frase[i-1] != ' ':
        cuenta+=1

    if frase[-1] == ' ':
        cuenta = cuenta - 1

    palabras = cuenta + 1

print(palabras)