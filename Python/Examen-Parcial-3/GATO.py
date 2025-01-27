# Galilea Peralta Contreras.
# 26 de enero del 2025.
# Descripción:
from random import choice

X = "X"
O = "0"
NINGUNO = "Ninguno gano"


def menu() -> int:
    print("***  Juego del gato  ***")
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


def submenu() -> str:
    print("1) O")
    print("2) X")
    marcador = input("Elige una opción: ")

    while not marcador.isnumeric() or not (marcador == '1' or marcador == '2'):
        print("Opción invalida")
        print("___________________________________________________________________")
        print()
        marcador = input("Intenta nuevamente: ")
        print()

    if marcador == 1:
        marcador = X
        marcador2 = O
    else:
        marcador = O
        marcador2 = X
    return str(marcador, marcador2)


def mostrartablero(lista: list[str]):
    matriz = []
    for i in range(0, 9):
        matriz.append(lista[i])

    espacio = " "
    raya_horizontal = "_"
    raya_vertical = "|"

    for i in range(0, 3):
        print(matriz[i + (i * 2)], raya_vertical, matriz[i + 1 + (i * 2)], raya_vertical, matriz[i + 2 + (i * 2)])
        print(raya_horizontal * 9)


def eleccion_del_jugador() -> int:
    opcion_del_jugador = input("Elija una posición: ")

    while not opcion_del_jugador.isnumeric() or not (
            opcion_del_jugador == '0' or opcion_del_jugador == '1' or opcion_del_jugador == '2' or opcion_del_jugador == '3' or opcion_del_jugador == '4' or opcion_del_jugador == '5' or opcion_del_jugador == '6' or opcion_del_jugador == '7' or opcion_del_jugador == '8'):
        print("Opción invalida")
        opcion_del_jugador = input("Intenta nuevamente: ")
    opcion_del_jugador = int(opcion_del_jugador)
    return int(opcion_del_jugador)


def comparacion(matriz: list[str]):
    i = 0
    gato = {(X, X, X): 1,
            (O, O, O): 2}
    while i <= 3:
        gato.get((matriz[i + (i * 2)], matriz[i + 1 + (i * 2)], matriz[i + 2 + (i * 2)), NINGUNO)


def verificar_sin_repeticiones_del_jugador(matriz: list[str]) -> int:
    opcion_del_jugador = eleccion_del_jugador()
    while matriz[opcion_del_jugador] != ' ':
        print("Opción repetirá.")
        print("Vuelva a intentar.")
        opcion_del_jugador = eleccion_del_jugador()
    return int(opcion_del_jugador)


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
            print("Las posiciones del tablero son: ")
            mostrartablero(posiciones)

            if jugador == O:
                opcion_del_jugador = verificar_sin_repeticiones_del_jugador(matriz)
                matriz[opcion_del_jugador] = jugador
                opcion_del_CPU = choice(posiciones)

                while matriz[opcion_del_CPU] != ' ':
                    opcion_del_CPU = choice(posiciones)

                matriz[opcion_del_CPU] = cpu

                comparacion(matriz)







        else:
            print()
    print("___________________________________________________________________")