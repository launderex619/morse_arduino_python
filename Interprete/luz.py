import constantes
def luz():
    print('-------------------------')
    print('1.- Emitir')
    print('2.- Recibir')
    print('-------------------------')
    try:
        opcion = int(raw_input())
        if (opcion == 1):
            cadena = raw_input("Ingresa la cadena: ")
            constantes.enviaCadArduinoLuz(cadena)

        elif (opcion == 2):
    # Pendiente leer luz
    except ValueError:
        print('Valor no valido')

    pass
