# Galilea Peralta Contreras.
# 26 de enero del 2025.
# Descripción:
from random import choice

PRIMERO = "X"
SEGUNDO = "0"
NINGUNO = "Ninguno gano"


def menu() -> int:
    print("***  Juego de 4 en uno ***")
    print("0) Salir.")
    print("1) Jugar vs la CPU.")
    print("2) Jugar vs  otro jugador.")
    print()
    opcion = input("Elije una opción: ")

    while not opcion.isnumeric() or not (opcion == '0' or opcion == '1' or opcion == '2'):
        print("Opción invalida")
        print("___________________________________________________________________")
        print()
        opcion = input("Intenta nuevamente: ")
        print()
    return int(opcion)


def submenu() -> tuple[str]:
    print("1) O")
    print("2) X")
    marcador_jugador = input("Elige una opción: ")

    while not marcador_jugador.isnumeric() or not (marcador_jugador == '1' or marcador_jugador == '2'):
        print("Opción invalida")
        print("___________________________________________________________________")
        print()
        marcador_jugador = input("Intenta nuevamente: ")
        print()

    if marcador_jugador == 1:
        marcador_jugador = PRIMERO
        marcador_cpu = SEGUNDO
    else:
        marcador_jugador = SEGUNDO
        marcador_cpu = PRIMERO
    return marcador_jugador, marcador_cpu


def mostrar_tablero(lista: list[str]):
    matriz = []
    for i in range(0, 9):
        matriz.append(lista[i])

    espacio = " "
    raya_horizontal = "_"
    raya_vertical = "|"

    for i in range(0, 3):
        print(matriz[i + (i * 2)], raya_vertical, matriz[i + 1 + (i * 2)], raya_vertical, matriz[i + 2 + (i * 2)])
        print(raya_horizontal * 9)


if __name__ == '__main__':
    matriz = []
    posiciones = []
    opcion = None

    while opcion != 0:
        for i in range(0, 9):
            matriz.append(' ')
        for i in range(0, 9):
            posiciones.append(str(i))

        opcion = menu()
        if opcion == 0:
            print("Fin del programa.")
        elif opcion == 1:
            jugador, cpu = submenu()
            mostrar_tablero(posiciones)

        else:
            print()
    print("___________________________________________________________________")
