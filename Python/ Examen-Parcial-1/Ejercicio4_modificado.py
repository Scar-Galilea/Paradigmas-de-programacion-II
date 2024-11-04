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
Numero_adivinar =  randint(1, 100)

print("     1) Facil.")
print("     2) Mediano.")
print("     3) Dificultad")
Dificultad = int(input("Ingrese la dificultad: "))

Contador = 0;

while Contador != 1:
    if Dificultad == 1:
        Numero_de_final = 10
        Numero_adivinar =  randint(1, 50)
        Contador = 1
    elif Dificultad == 2:
        Numero_de_final = 5
        Numero_adivinar =  randint(1, 100)
        Contador = 1
    elif Dificultad == 3:
        Numero_de_final = 4
        Numero_adivinar =  randint(1, 110)
        Contador = 1
    else:
        print("Dificultad no reconocida, vuelva intentarlo")
        Contador = 0
print()
while Intentos <= Numero_de_final:
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

if Numero_adivinar != Numero_del_usuario:
    print("Perdiste. El número era: ",Numero_adivinar)


print()
print("Fin del programa")
