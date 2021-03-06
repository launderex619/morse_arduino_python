import constantes, threading
import re

def leerArduinoLuz(running):
     constantes.filtro = []
     while running.is_set():
        cadenaMorse = constantes.arduino.readline()
        print(cadenaMorse)
        cadenaMorse = int(cadenaMorse[:3])
        if(cadenaMorse > 400):
            cadenaMorse = 1
        else:
            cadenaMorse = 0
        constantes.filtro.append(cadenaMorse)

def analizarLuz(lista):
    listaTentativa = []
    unidades = len(lista) /50
    posicionEnLista = 0
    while(unidades > 0):
        contador = 0
        iterador = lista[posicionEnLista:posicionEnLista+50]
        for x in iterador:
            if(x == 1):
                contador += 1
        contador = contador / 50.0
        if (contador > .3):
            contador = 1
        else:
            contador = 0
        listaTentativa.append(contador)
        posicionEnLista += 50
        contador = 0
        unidades -= 1
        print('binarios recolectados: ')
        print(listaTentativa)
        listaTentativa = constantes.numerosListaANumerosAscii(listaTentativa)
        print(constantes.decodifica(listaTentativa))

def luz():
    print('-------------------------')
    print('1.- Emitir')
    print('2.- Recibir')
    print('-------------------------')
    try:
        opcion = int(raw_input())
        if (opcion == 1):
            while True:
                cadena = raw_input("Ingresa la cadena: ")
                if(re.findall("^[a-zA-Z0-9]+$",cadena)):
                    break
                else:
                    print("Ingrese solo caracteres aceptados")
            constantes.enviaCadArduinoLuz(cadena)

        elif (opcion == 2):
            print('presiona ENTER para salir del modo escucha\n')
            estadoReciviendo = True
            constantes.arduino.write(constantes.modoEscuchaLuz)
            while True:
                a = constantes.arduino.readline()[:3]
                a = int(a)
                if(a > 300):
                    break
            print("luz detectada, comenzando el analisis....")
            running.set()
            thread = threading.Thread(target=leerArduinoLuz, args=(running,))
            thread.start()
            while True:
                raw_input() #Cuando se presione enter se para
                running.clear()
                thread.join()
                break
            print('limpiando ruido...')
            analizarLuz(constantes.filtro)
    except ValueError:
        print('Valor no valido')

    pass
