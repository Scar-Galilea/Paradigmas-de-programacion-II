#Galilea Peralta Contreras.
#03 de noviembre de 2024.
#Descripción:
## Programa para mostrar una cuenta hasta un número ingresado por el usuario, reemplazando ciertos números con palabras específicas.

"""
Este programa determina el área y el perímetro de un rectángulo o de un círculo.
Muestre el siguiente menú:

1) Calcular el área de un rectángulo.
2) Calcular el perímetro de un rectángulo.
3) Calcular el área de un círculo.
4) Calcular el perímetro de un círculo.
0) Salir.
Cualquier otro caso -> Mostrar un mensaje de "opción no válida".

Para ello:

a) Muestre el menú anterior en consola.

b) En caso de calcular un área o perímetro, solicite al usuario los valores requeridos (flotantes).

c) Utilice la lógica adecuada para calcular lo solicitado. Asuma pi = 3.1416.

d) Imprima el resultado en la consola. Nota: muestre únicamente 3 decimales en todos los casos.

e) Repita el menú hasta salir.
"""

Contador_1 = 1
while Contador_1 != 0:
    print("*** Programa que calcula el área y el perímetro **+")
    print("1) Calcular el área de un rectángulo.")
    print("2) Calcular el perímetro de un rectángulo..")
    print("3) Calcular el área de un círculo.")
    print("4)  Calcular el perímetro de un círculo.")
    print("0) Salir")
    print()
    Opcion = int(input("Ingresa una opción: "))
    Contador_1 = Opcion

    if Opcion != 0:
        if Opcion == 1:
            print()
            Base = float(input("Ingrese la base: "))
            Altura = float(input("Ingrese la altura: "))
            Area = Base * Altura
            print()
            print(f"El area es: {Area:.3f}")
            print("-----------------------------------")
            print()
        elif Opcion == 2:
            print()
            Base = float(input("Ingrese la base: "))
            Altura = float(input("Ingrese la altura: "))
            Perimetro = (2 * Altura) + (2 * Base)
            print()
            print(f"El perimetro es: {Perimetro:.3f}")
            print("------------------------------------")
            print()
        elif Opcion == 3:
            print()
            Radio = float(input("Ingrese la radio: "))
            Area = 3.1416 * (Radio * Radio)
            print()
            print(f"El area es: {Area:.3f}")
            print("-----------------------------------")
            print()
        elif Opcion == 4:
            print()
            Radio = float(input("Ingrese la radio: "))
            Perimetro = 2 * 3.1416 * Radio
            print(f"El perimetro es: {Perimetro:.3f}")
            print(f"El perimetro es: {Perimetro:.3f}")
            print("-----------------------------------")
            print()
        else:
            print()
            print("Opcion invalida")
            print("-----------------------------------")
            print()
print()
print("Salio del programa")
