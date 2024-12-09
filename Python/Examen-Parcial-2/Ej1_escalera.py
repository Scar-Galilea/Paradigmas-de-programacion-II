#Galilea Peralta Contreras.
#07 de diciembre del 2024.
#Descripción:
#Este programa dibuja una escalera ascendente o descendente según el número de escalones ingresado por el usuario.
# Si el número es positivo, se dibuja una escalera ascendente; si es negativo, se dibuja una descendente.
# Si se ingresa un 0, el programa termina.

"""
Instrucciones:
Escribe un programa de nombre Ej1_escalera.py que realice lo que se indica en la descripción del programa.
Comparte el enlace de GitHub en la caja de texto al final de la pregunta.
Descripción del programa:
Este programa dibuja una escalera, en donde el usuario ingresa el número de escalones.
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

#Función para dibujar una escalera descendente
def Negativo(Numero_de_filas):
    Numero_de_filas = Numero_de_filas * -1  #Convierte el número negativo a positivo.
    Raya = "_" #Representa el escalón horizontal.
    Palo = "|"  #Representa el escalón vertical.
    print("Forma 1:")
    for j in range(1, Numero_de_filas + 1): #Ciclo para generar cada escalón.
        Espacio = " " * j #Incrementa el espacio al principio de cada línea.
        print(f"{Raya}")
        print(f"{Espacio}{Palo}",end="")
    print(f"{Raya}")  #Finaliza con una última raya al final de la escalera.

#Función para dibujar una escalera ascendente
def Positivo(Numero_de_filas):
    Raya = "_" #Representa el escalón horizontal.
    Palo = "|" #Representa el escalón vertical.
    Contador = Numero_de_filas #Inicia desde el número total de escalones.
    Ep = " " #Espacios para alinear la escalera.
    print(f"{Ep * (Contador + 2)}{Raya}") #Dibuja la línea inicial de la parte superior.
    for j in range(1, Numero_de_filas + 1):
        Espacio = " " * Contador  #Decrementa el espacio en cada escalón.
        print(f"{Espacio}{Raya}",end="")
        print(f"{Palo}")
        Contador -= 1  #Reduce el contador para ajustar el espacio en el siguiente escalón.


#Programa principal:
Numero_de_filas = None #Variable para almacenar el número de escalones.
while Numero_de_filas != 0: #Ciclo principal que continúa mientras no se ingrese un 0.
    print()
    print("  ***  Ejercicio 1. La escalera.  ***")
    Numero_de_filas = int(input("Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir:  "))

    if Numero_de_filas == 0:  #Opción para salir del programa.
        print("Fin del programa.")
    elif Numero_de_filas < 0: #Si el número es negativo, dibuja una escalera descendente.
        Negativo(Numero_de_filas)
    elif Numero_de_filas > 0: #Si el número es positivo, dibuja una escalera ascendente.
        Positivo(Numero_de_filas)
    else:
        print("Opción incorrecta.")
    print("________________________________________________________________")


