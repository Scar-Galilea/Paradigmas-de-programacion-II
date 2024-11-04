#Galilea Peralta Contreras.
#03 de noviembre de 2024.
#Descripción:
#  Este programa permite al usuario jugar a un juego de adivinanza de números donde intenta adivinar un número aleatorio generado por la CPU en el rango de 1 a 100.
"""
Este programa es un juego en donde el usuario intente adivinar un número secreto.

Para ello:

a) El número a adivinar es un número aleatorio entre 1 y 100.

b) El jugador tendrá 5 intentos para encontrar el número.

c) Como pista, el juego indicará si el número a adivinar es menor o mayor al número ingresado, si el número no es el correcto.

d) Si el jugador adivina el número, el juego muestra un mensaje de felicitación y el número de intentos.

e) Si el jugador no adivina el número, el juego muestra un mensaje con el número.
"""
from random import randint  # Importamos la función randint para generar el número aleatorio.

# Inicialización de variables.

Intentos = 1 # Contador de intentos.
Numero_adivinar =  randint(1, 100)  # La CPU elige un número aleatorio entre 1 y 100.

while Intentos <= 5 : # Bucle de intentos limitados a un máximo de 5.
    print("*** Juego del adivinador. **+")
    print(f"Número de intentos: {Intentos}", end = " ")

    # Solicita al usuario que ingrese un número
    Numero_del_usuario = int(input("Ingresa un número (1-100): "))

    # Verifica si el número del usuario coincide con el número a adivinar.
    if Numero_adivinar == Numero_del_usuario:
        print()
        print(f"¡Felicidades!, adivinaste en {Intentos} intentos.")
        Intentos = 7 #Finaliza el bucle si el usuario adivina correctamente.
    elif Numero_del_usuario < Numero_adivinar :
        print()
        print("El número a adivinar es mayor.") #Indicación de que el número es mayor.
        Intentos += 1
        print()
    else:
        print()
        print("El número a adivinar es menor.") # Indicación de que el número es menor
        Intentos += 1
        print()

    if Intentos == 6: #Este if funciona para verificar si el usuario dio 5 intentos.
    #Ya que al finalizar una de las opciones se le sumará 1. por eso lo dará  6.
        print("Perdiste. El número era: ",Numero_adivinar)


print()
print("Fin del programa")
