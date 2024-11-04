#Galilea Peralta Contreras.
#03 de noviembre de 2024.
#Descripción:
## Programa para mostrar una cuenta hasta un número ingresado por el usuario, reemplazando ciertos números con palabras específicas.

"""
Este programa es el famoso juego de "piedra, papel o tijera", en donde el contrincante es la CPU. La opción de la CPU se escogerá de forma aleatorio con la función randint().

El juego mostrará las victorias del jugador, los partidos empatados y las victorias del CPU. Además, mostrará el siguiente menú:

1) Piedra.
2) Papel.
3) Tijera.
0) Salir.
Cualquier otro caso -> Mostrar un mensaje de "opción no válida".

Para ello:

a) Muestre la cantidad de victorias, empates y derrotas.

b) Pida al usuario una opción del menú.

c) Realice la lógica adecuada para calcular al ganador.

d) Muestre en la consola la elección del jugador, del CPU y el resultado.

e) Repita nuevamente el menú hasta salir.
"""
from random import random, randint

Contador_1 = 1
Victorias_del_jugador = 0
Empates = 0
Victorias_del_CPU = 0

while Contador_1 != 0:
    print("*** Juego de piedra, papel o tijera. **+")
    print(f"Victorias dej jugador: {Victorias_del_jugador}, empates: {Empates} y victorias del CPU: {Victorias_del_CPU}  ")
    print("     1) Piedra.")
    print("     2) Papel.")
    print("     3) Tijera.")
    print("     0) Salir")
    print()
    Opcion = int(input("Ingresa una opción: "))
    Contador_1 = Opcion
    Opcion_del_CPU = randint(1, 3)

    if Contador_1 != 0:
        if Opcion == 1 and Opcion_del_CPU == 1:
            print()
            Empates += 1
            print(f"Jugador: piedra. CPU: piedra. El resultado es empate.")
            print("------------------------------------")
            print()

        elif Opcion == 2 and Opcion_del_CPU == 2:
            print()
            print(f"Jugador: papel. CPU: papel. El resultado es empate.")
            Empates += 1
            print("------------------------------------")
            print()
        elif Opcion == 3 and Opcion_del_CPU == 3:
            print()
            print(f"Jugador: tijera. CPU: tijera. El resultado es empate.")
            Empates += 1
            print("------------------------------------")
            print()
        elif Opcion == 1 and Opcion_del_CPU == 2:
            print()
            print(f"Jugador: piedra. CPU: papel. El ganador es el CPU.")
            Victorias_del_CPU += 1
            print("------------------------------------")
            print()
        elif Opcion == 1 and Opcion_del_CPU == 3:
            print()
            print(f"Jugador: piedra. CPU: tijera. El ganador es el jugador.")
            Victorias_del_jugador += 1
            print("------------------------------------")
            print()
        elif Opcion == 2 and Opcion_del_CPU == 1:
            print()
            print(f"Jugador: papel. CPU: piedra. El ganador es el jugador.")
            Victorias_del_jugador += 1
            print("------------------------------------")
            print()
        elif Opcion == 2 and Opcion_del_CPU == 3:
            print()
            print(f"Jugador: papel. CPU: tijera. El ganador es el CPU.")
            Victorias_del_CPU += 1
            print("------------------------------------")
            print()
        elif Opcion == 3 and Opcion_del_CPU == 1:
            print()
            print(f"Jugador: tijera. CPU: piedra. El ganador es el CPU.")
            Victorias_del_CPU += 1
            print("------------------------------------")
            print()
        elif Opcion == 3 and Opcion_del_CPU == 2:
            print()
            print(f"Jugador: tijera. CPU: papel. El ganador es el jugador.")
            Victorias_del_jugador += 1
            print("------------------------------------")
            print()
        else:
            print()
            print("Opcion invalida")
            print("-----------------------------------")
            print()
print()
print("Salio del programa")
