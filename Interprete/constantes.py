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
    for x in lista:
        if(x == 1):
            if(acarreo == 0):
                pass
    return lista