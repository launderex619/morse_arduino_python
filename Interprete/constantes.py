import serial,threading

programaEjecutandose = True
modoEscuchaSonido = '7'
modoEscuchaLuz = '8'
arduino = serial.Serial('/dev/ttyUSB0', 9600)
filtro = []
tiempoEsperaCiclo = 20
cadenaMorse = ""
punto = 1
raya = 2
espacioLetra = 3
espacioPalabra = 4
morseAscii = {
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z",
        "-----": "0",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
        "@": " "
        }
def numerosListaANumerosAscii(lista):
    punto = 1
    raya = 2
    espacioLetra = 3
    espacioPalabra = 4
    listaMorse = []
    acarreo = 0
    try:
        i = 0
        while i  < (len(lista)):
            if(lista[i] == 1):
                if(i + 1 < len(lista)):
                    if(lista[i + 1] == 1 ):
                        if(i + 2 < len(lista)):
                            if(lista[i + 2] == 1):
                                listaMorse.append(raya)
                                i += 2
                            else:
                                i += 1
                                listaMorse.append(punto)
            else:
                if(i + 1 < len(lista)):
                    if(lista[i + 1] == 0):
                        if(i + 2 < len(lista)):
                            if(lista[i + 2] == 0):
                                listaMorse.append(espacioPalabra)
                                i += 2
                            else:
                                listaMorse.append(espacioLetra)
                                i += 1
                else:
                    listaMorse.append(espacioLetra)
            i+=1
    except:
        pass
    return listaMorse

def decodifica(lista):
    cad = ""
    oracion = ""
    for x in lista:
        if x == 1:
            cad += "."
        elif x == 2:
            cad += "-"
        elif x == 3 and cad != "":
            oracion += convierte(cad)
            cad = ""
        elif x == 4:
            oracion += " "
    if cad != "":
        oracion += convierte(cad)
    return oracion
def convierte( cadena ):
    switcher = {
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z",
        "-----": "0",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9"

    }
    return switcher.get(cadena)

asciiMorse = dict(map(reversed, morseAscii.items()))
def listaAscii(lista):
    cad = ""
    oracion = ""
    for x in lista:
        if x == punto:
            cad += "."
        elif x == raya:
            cad += "-"
        elif x == espacioLetra:
            oracion += morseAscii.get(cad)
            cad = ""
        elif x == espacioPalabra:
            oracion += " "
    if cad != "":
        oracion += morseAscii.get(cad)
    return oracion

def enviaCadArduinoSonido(cadena):
    for c in cadena:
        morse = asciiMorse.get(c)
        print(morse)
        for m in morse:
            if m == '.':
                arduino.write('1')
            elif m == '-':
                arduino.write('2')
            elif m == '@':
                arduino.write('3')
    arduino.write('3')
def enviaCadArduinoLuz(cadena):
    for c in cadena:
        morse = asciiMorse.get(c)
        print(morse)
        for m in morse:
            if m == '.':
                arduino.write('4')
            elif m == '-':
                arduino.write('5')
            elif m == '@':
                arduino.write('6')
    arduino.write('6')
