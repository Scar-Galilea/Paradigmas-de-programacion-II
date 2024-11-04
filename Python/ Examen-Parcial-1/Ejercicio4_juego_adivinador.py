#Galilea Peralta Contreras.
#03 de noviembre de 2024.
#Descripción:
## Programa para mostrar una cuenta hasta un número ingresado por el usuario, reemplazando ciertos números con palabras específicas.

"""
Este programa es un juego en donde el usuario intente adivinar un número secreto.

Para ello:

a) El número a adivinar es un número aleatorio entre 1 y 100.

b) El jugador tendrá 5 intentos para encontrar el número.

c) Como pista, el juego indicará si el número a adivinar es menor o mayor al número ingresado, si el número no es el correcto.

d) Si el jugador adivina el número, el juego muestra un mensaje de felicitación y el número de intentos.

e) Si el jugador no adivina el número, el juego muestra un mensaje con el número.
"""
from random import randint

Intentos = 1
while Intentos <= 5 :
    print("*** Juego del adivinador. **+")
    print(f"Número de intentos: {Intentos}", end = " ")

    Numero_del_usuario = int(input("Ingresa un número (1-100): "))

    Numero_adivinar =  randint(1, 100)

    if Numero_adivinar == Numero_del_usuario:
        print()
        print(f"¡Felicidades!, adivinaste en {Intentos} intentos.")
        Intentos = 6
    elif Numero_del_usuario < Numero_adivinar :
        print()
        print("El número a adivinar es mayor.")
        Intentos += 1
        print()
    else:
        print()
        print("El número a adivinar es menor.")
        Intentos += 1
        print()

    if Intentos == 6:
        print("Perdiste. El número era: ",Numero_adivinar)


print()
print("Fin del programa")
