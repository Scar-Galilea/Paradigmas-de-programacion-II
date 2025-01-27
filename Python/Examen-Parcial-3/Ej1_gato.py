# Galilea Peralta Contreras.
# 26 de enero del 2025.
# Descripción:
from random import choice

PRIMERO = "X"
SEGUNDO = "0"

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

def verificar(matriz:list[str]) -> int:
    opcion_del_jugador = input("Elija una posición: ")
    while not opcion_del_jugador.isnumeric() or not ('0','1','3','4','5','6','7','8'):
        print("Opción invalida")
        opcion_del_jugador = input("Intenta nuevamente: ")
    opcion_del_jugador = int(opcion_del_jugador)
    while matriz[opcion_del_jugador] != ' ' :
        print("Opción repetida.")
        opcion_del_jugador = input("Intenta nuevamente: ")
        while not opcion_del_jugador.isnumeric() or not ('0', '1', '3', '4', '5', '6', '7', '8'):
            print("Opción invalida")
            opcion_del_jugador = input("Intenta nuevamente: ")

    return int(opcion_del_jugador)

def comparacion(matriz: list[str])-> int | None:
    marcadores = None
    i = 0
    gato = {(X, X, X): 1,
            (O, O, O): 2}

    for i in range(0, 3):
        marcadores = gato.get((matriz[i+2*i],matriz[i+1+i*2],matriz[i+2+i*2]),None)
        if marcadores == 1 or marcadores == 2:
            return int(marcadores)
        marcadores = gato.get((matriz[i + 2*i], matriz[3+i], matriz[6+i]), None)
        if marcadores == 1 or marcadores == 2:
            return int(marcadores)

    marcadores = gato.get((matriz[i], matriz[4], matriz[8]), None)
    if marcadores == 1 or marcadores == 2:
        return int(marcadores)
    marcadores = gato.get((matriz[2], matriz[4], matriz[6]), None)
    if marcadores == 1 or marcadores == 2:
        return int(marcadores)

if __name__ == '__main__':
    matriz = []
    posiciones = []
    lleno = 0
    opcion = None

    while opcion != 0:
        for i in range(0, 9):
            posiciones.append(int(i))

        opcion = menu()
        if opcion == 0:
            print("Fin del programa.")
        elif opcion == 1:
            bandera = 0
            jugador, cpu = submenu()
            mostrar_tablero(posiciones)
            for i in range(0, 9):
                matriz.append(' ')

            while bandera == 0 or lleno == 0:
                eleccion_del_jugador = verificar(matriz)
                matriz = matriz[eleccion_del_jugador-1]
                opcion_del_CPU = choice(posiciones)

                print(opcion_del_CPU)
                print(eleccion_del_jugador)
                print()
                while matriz[opcion_del_CPU] != ' ':
                    opcion_del_CPU = choice(posiciones)

                comparacion(matriz)

                for l in matriz:
                    if l != matriz:
                        bandera = 0
                        break
                    else:
                        bandera = 1
                mostrar_tablero(matriz)









        else:
            print()
    print("___________________________________________________________________")
