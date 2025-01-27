#Galilea Peralta Contreras.
#26 de enero del 2025.
#Descripción:

def menu() -> int:
    print("  ***  Menú de juegos  ***")
    print("0) Salir.")
    print("1) Juego del gato.")
    print("2) Juego del ahorcado.")
    print("3) Juego de 4 en raya.")
    print()
    opcion = input("Elije una opción: ")

    while not opcion.isnumeric() or not (opcion == '0' or opcion == '1' or opcion == '2' or opcion == '3'):
        print("Opción invalida")
        print("___________________________________________________________________")
        print()
        opcion = input("Intenta nuevamente: ")
        print()
    return int(opcion)


if __name__ == '__main__':
    opcion = None

    while opcion != 0:
        opcion = menu()
        if opcion == 0:
            print("Fin del programa.")
        elif opcion == 1:
            print()
        elif opcion == 2:
            print()
        else:
            print()
    print("___________________________________________________________________")

