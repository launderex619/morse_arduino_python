import serial,threading, time

programaEjecutandose = True
modoEscuchaSonido = '7'
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

def enviaCadArduino(cadena):
    for c in cadena:
        morse = asciiMorse.get(c)
        for m in morse:
            if m == '.':
                arduino.write(1)
                time.sleep(2)
            elif m == '-':
                arduino.write(2)
                time.sleep(4)
            elif m == '@':
                arduino.write(3)
                time.sleep(3)
