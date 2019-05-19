import serial,threading
import constantes, sonido, luz

def imprimeMenu():
    print('============= Morse ================')
    print('1.- Comunicacion por sonido')
    print('2.- Comunicacion por luz')
    print('3.- Salir')
    return


if __name__ == "__main__":
    while constantes.programaEjecutandose:
        sonido.running = threading.Event()
        #print(arduino.readline());
        imprimeMenu()
        try:
            opcion = int(raw_input())
            if(opcion == 1):
                sonido.sonido()
            elif(opcion == 2):
                luz.luz()
            elif(opcion == 3):
                constantes.programaEjecutandose = False

        except ValueError:
            print('Valor no valido')