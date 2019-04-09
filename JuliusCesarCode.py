f_in = open("lectura", "r")
f_out = open("Escritura", "w")

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MAX_COD_LVL = 26


def getMode(): #Función para elegir si desencriptamos o encriptamos
    while True:
        print("¿Quieres encriptar(e) o desencriptar(d) tu mensaje?")
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split(): #Comprobamos si el string guardado en mode existe en la lista que nos devuelve 'encrypt e decrypt d'.split()
            return mode
        else:
            print("Introduce 'Encriptar' o 'Desencriptar'.")


def getText():
    linea = f_in.readline()
    return linea

def getLvl(): #Definimos el Nivel de encriptación que deseamos
    lvl = 0
    while True: #Usamos while para asegurarnos de introducir un nivel correcto
        print("Introduce el nivel de encriptación()1-%s"%(MAX_COD_LVL))
        lvl = int(input()) #Hacemos que el nvl sea un integer.
        if(lvl>=1 and lvl<=MAX_COD_LVL):
            return lvl

def getTransText(mode, text, lvl): #mode sirve para saber si vamos a encriptar o desencriptar, text es el texto a encriptar, y lvl es el nivel de encriptacion
    if mode[0] == 'd': #comprobamos que la primera letra de la variable mode sea 'd', para asi saber si estamos en el modo desencriptar.
        lvl = -lvl
    traducir = "" #El resultado

    for symbol in text: #iteramos sobre cada letra del texto que tenemos
        if symbol.isalpha(): #isalpha se usa para así encriptar solo letras, por lo tanto cualquier otro elemento se quedará como tal
            num = ord(symbol)
            num += lvl

            if symbol.isupper():
                if num > ord("Z"):
                    num -= 26
                elif num < ord("A"):
                    num += 26

            elif symbol.islower():
                if num > ord("z"):
                    num -= 26
                elif num < ord("a"):
                    num += 26

            traducir += chr(num)
        else:
            traducir += symbol

    return traducir


mode = getMode()
text = getText()
lvl = getLvl()
f_out.write(getTransText(mode, text, lvl))
