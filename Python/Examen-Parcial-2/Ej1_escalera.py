#Galilea Peralta Contreras.
#07 de diciembre del 2024.
#Descripción:

"""
Instrucciones:
Escribe un programa de nombre Ej1_escalera.py que realice lo que se indica en la descripción del programa.
Comparte el enlace de GitHub en la caja de texto al final de la pregunta.
Descripción del programa:
Este programa dibuja una escalera, en donde el usuario ingresa el número de escalores.
Si el número es positivo, la escalera será ascendente. Un ejemplo cuando se ingresa un valor de 4:        _
      _|
    _|
  _|
_|

Si el número es negativo, la escalera será descendente. Un ejemplo cuando se ingresa un valor de -4:

_
 |_
   |_
     |_
       |_

Si el número es cero, se deberá salir del programa.
Se debe mostrar la siguiente pantalla:
  ***  Ejercicio 1. La escalera.  ***
Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir:
Cualquier otro caso -> Opción no válida.
Para ello:
a) Solicite el número de escalones utilizando un ciclo.
b) Muestre la escalera utilizando la lógica adecuada. Se requiere utilizar funciones para dibujar las escaleras para considerar el ejercicio como completo.
"""
from xml.dom.minidom import ProcessingInstruction


def Negativo(Numero_de_filas):
    Numero_de_filas =   Numero_de_filas * -1
    Raya = "_"
    Palo = "|"
    print("Forma 1:")
    for j in range(1, Numero_de_filas + 1):
        Espacio = " " * j
        print(f"{Raya}")
        print(f"{Espacio}{Palo}",end="")
    print(f"{Raya}")

def Positivo(Numero_de_filas):
    Raya = "_"
    Palo = "|"
    Contador = Numero_de_filas
    Ep = " "
    print(f"{Ep * (Contador + 2)}{Raya}")
    for j in range(1, Numero_de_filas + 1):
        Espacio = " " * Contador
        print(f"{Espacio}{Raya}",end="")
        print(f"{Palo}")
        Contador -= 1


Numero_de_filas = None
while Numero_de_filas != 0:
    print()
    print("  ***  Ejercicio 1. La escalera.  ***")
    Numero_de_filas = int(input("Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir:  "))

    if Numero_de_filas == 0:  #Opción para salir del programa.
        print("Fin del programa")
    elif Numero_de_filas < 0:
        Negativo(Numero_de_filas)
    elif Numero_de_filas > 0:
        Positivo(Numero_de_filas)
    else:
        print("Opción incorrecta.")
    print("________________________________________________________________")


