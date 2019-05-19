import serial,threading

def leerArduinoSonido(running):
    while running.is_set():
        cadenaMorse = arduino.readline()
        print(cadenaMorse)
        filtro.append(cadenaMorse)


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

def analizarSonido(lista):
    listaTentativa = []
    unidades = len(lista) /50
    posicionEnLista = 0
    while(unidades > 0):
        contador = 0
        iterador = lista[posicionEnLista:posicionEnLista+50]
        for x in iterador:
            if(x == 1):
                contador += 1
        contador = contador / 50
        if (contador > .5):
            contador = 1
        else:
            contador = 0
        listaTentativa.append(contador)
        posicionEnLista += 1
        contador = 0
        unidades -= 1
    listaTentativa = numerosListaANumerosAscii(listaTentativa)


def imprimeMenu():
    print('============= Morse ================')
    print('1.- Comunicacion por sonido')
    print('2.- Comunicacion por luz')
    print('3.- Salir')
    return

def sonido():
    print('-------------------------')
    print('1.- Emitir')
    print('2.- Recibir')
    print('-------------------------')
    try:
        opcion = int(raw_input())
        if(opcion == 1):
            cadena = raw_input()
            #pendiente emitir la cadena

        elif(opcion == 2):
            print('presiona ENTER para salir del modo escucha\n')
            estadoReciviendo = True
            arduino.write(modoEscuchaSonido)
            while True:
                a = arduino.readline()[:1]
                if(a == '1'):
                    break
            running.set()
            thread = threading.Thread(target=leerArduinoSonido, args=(running,))
            thread.start()
            while True:
                raw_input() #Cuando se presione enter se para
                running.clear()
                thread.join()
                break
            print(cadenaMorse)
            analizarSonido(cadenaMorse)
    except ValueError:
        print('Valor no valido')

    pass

def luz():
    pass

while programaEjecutandose:
    running = threading.Event()
    #print(arduino.readline());
    imprimeMenu()
    try:
        opcion = int(raw_input())
        if(opcion == 1):
            sonido()
        elif(opcion == 2):
            luz()
        elif(opcion == 3):
            programaEjecutandose = False

    except ValueError:
        print('Valor no valido')
#arduino.write(raw_input() + "\n")
