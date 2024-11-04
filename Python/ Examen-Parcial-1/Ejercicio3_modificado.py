#Galilea Peralta Contreras.
#03 de noviembre de 2024.
#Descripción:
## Programa que simula el juego de "Piedra, Papel o Tijera" contra la CPU, donde la CPU elige su opción aleatoriamente
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

while Contador_1 != "0":
    print("*** Juego de piedra, papel o tijera. **+")
    print(f"Victorias del jugador: {Victorias_del_jugador}, empates: {Empates} y victorias del CPU: {Victorias_del_CPU}  ")
    print("     1) Piedra.")
    print("     2) Papel.")
    print("     3) Tijera.")
    print("     0) Salir")
    print()
    Opcion = (input("Ingresa una opción: "))
    Contador_1 = Opcion  #Asigna la opción a contador para mantener el bucle activo.
    Opcion_del_CPU = randint(1, 3)  #La CPU elige aleatoriamente entre 1, 2 y 3.
    Opcion = Opcion.lower()

    #Comprobación de condiciones para jugar o salir.
    if Contador_1 != "0":
        # Si ambos eligen lo mismo, es empate.
        if Opcion == "piedra" and Opcion_del_CPU == 1:
            print()
            print(f"Jugador: {Opcion} CPU: piedra resultado es empate.")
            Empates += 1
            print("------------------------------------")
            print()

        elif Opcion == "papel" and Opcion_del_CPU == 2:
            #Si ambos eligen lo mismo, es empate.
            print()
            print(f"Jugador: {Opcion}. CPU: papel. El resultado es empate.")
            Empates += 1
            print("------------------------------------")
            print()
        elif Opcion == "tijera" and Opcion_del_CPU == 3:
            # Si ambos eligen lo mismo, es empate.
            print()
            print(f"Jugador: {Opcion}. CPU: tijera. El resultado es empate.")
            Empates += 1
            print("------------------------------------")
            print()
        elif Opcion == "piedra" and Opcion_del_CPU == 2:
            print()
            print(f"Jugador: {Opcion}. CPU: papel. El ganador es el jugador.")
            Victorias_del_jugador += 1
            print("------------------------------------")
            print()
        elif Opcion == "piedra" and Opcion_del_CPU == 3:
            print()
            print(f"Jugador: {Opcion}. CPU: tijera. El ganador es el CPU")
            Victorias_del_CPU += 1
            print("------------------------------------")
            print()
        elif Opcion == "papel" and Opcion_del_CPU == 1:
            print()
            print(f"Jugador: {Opcion}. CPU: piedra. El ganador es el CPU.")
            Victorias_del_CPU += 1
            print("------------------------------------")
            print()
        elif Opcion == "papel" and Opcion_del_CPU == 3:
            print()
            print(f"Jugador: {Opcion}. CPU: tijera. El ganador es el jugador.")
            Victorias_del_jugador += 1
            print("------------------------------------")
            print()
        elif Opcion == "tijera" and Opcion_del_CPU == 1:
            print()
            print(f"Jugador: {Opcion}. CPU: piedra. El ganador es el jugador.")
            Victorias_del_jugador += 1
            print("------------------------------------")
            print()
        elif Opcion == "tijera" and Opcion_del_CPU == 2:
            print()
            print(f"Jugador: {Opcion}. CPU: papel. El ganador es el CPU.")
            Victorias_del_CPU += 1
            print("------------------------------------")
            print()
        else:
            print()
            print("Opción inválida")
            print("-----------------------------------")
            print()
print()
print("Salio del programa")
