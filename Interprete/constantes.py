import serial,threading

programaEjecutandose = True
modoEscuchaSonido = '7'
arduino = serial.Serial('/dev/ttyUSB0', 9600)
filtro = []
tiempoEsperaCiclo = 20
cadenaMorse = ""

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
                if(lista[i + 1] == 1):
                    if(lista[i + 2] == 1):
                        listaMorse.append(raya)
                        i += 2
                        continue
                    else:
                        i += 1
                        listaMorse.append(punto)
                        continue
                else:
                    continue
            else:
                if(lista[i + 1] == 0):
                    if(lista[i + 2] == 0):
                        listaMorse.append(espacioPalabra)
                        i += 2
                        continue
                    else:
                        listaMorse.append(espacioLetra)
                        i += 1
                        continue
                else:
                    listaMorse.append(espacioLetra)
    except:
        pass
    print(listaMorse)
    return listaMorse

def decodifica(lista):
    cad = ""
    oracion = ""
    for x in lista:
        if x == 1:
            cad += "."
        elif x == 2:
            cad += "-"
        elif x == 3:
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