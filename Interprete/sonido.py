import constantes
import threading

running = ""

def leerArduinoSonido(running):
    while running.is_set():
        cadenaMorse = constantes.arduino.readline()
        print(cadenaMorse)
        constantes.filtro.append(cadenaMorse)

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
    listaTentativa = constantes.numerosListaANumerosAscii(listaTentativa)

def sonido():
    print('-------------------------')
    print('1.- Emitir')
    print('2.- Recibir')
    print('-------------------------')
    try:
        opcion = int(raw_input())
        if(opcion == 1):
            cadena = raw_input("Ingresa la cadena: ")
            constantes.enviaCadArduinoSonido(cadena)
        elif(opcion == 2):
            print('presiona ENTER para salir del modo escucha\n')
            estadoReciviendo = True
            constantes.arduino.write(constantes.modoEscuchaSonido)
            while True:
                a = constantes.arduino.readline()[:1]
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
            print(constantes.cadenaMorse)
            analizarSonido(constantes.cadenaMorse)
    except ValueError:
        print('Valor no valido')

    pass
