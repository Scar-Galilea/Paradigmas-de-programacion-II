#Galilea Peralta Contreras.
#02 de noviembre de 2024.
#Descripción:
#Programa para mostrar una cuenta hasta un número ingresado por el usuario, reemplazando ciertos números con palabras específicas.

"""
Este programa imprime en consola los números, separados por comas, del 1 hasta un número ingresado por el usuario.

Sin embargo, se deben sustituir los siguientes valores:

3 o sus múltiplos por la palabra "Licenciatura".
5 y sus múltiplos por la palabra "Informática".
Múltiplos de 3 y 5 por la frase "Licenciatura en Informática" y se imprima un salto de línea en lugar de la coma.

Para ello:
a) Solicite un número en consola.
b) Realizar la lógica adecuada para imprimir los números o mensajes adecuados.
c) Mostrar los resultados en consola.

"""
print("*** Licentiatura en  informática ***")

# Solicitar al usuario el número final para la secuencia.
Número_final = int(input("Ingrese el número final de la cuenta: "))
print()

# Inicializamos la variable para empezar el conteo desde 1.
Número_inicial = 1

#Ciclo while para iterar desde 1 hasta el número ingresado por el usuario.
while Número_inicial <=  Número_final:

        #Condición para múltiplos de 3 y 5: imprime "Licenciatura en Informática" y hace salto de línea.
        if Número_inicial % 3 == 0 and Número_inicial % 5 == 0:
            print("Licenciatura en informática")

        #Condición para múltiplos de solo 3: imprime "Licenciatura".
        elif Número_inicial %3 == 0:
            print("Licenciatura,", end = " ")

        #Condición para múltiplos de solo 5: imprime "Informática".
        elif Número_inicial % 5 == 0:
            print("Informatica,", end = " ")

        #En caso de que el número no sea múltiplo de 3 ni de 5, lo imprime normalmente.
        else:
            print(Número_inicial, end = ", ")
        #En caso de que el número no sea múltiplo de 3 ni de 5, lo imprime normalmente.
        Número_inicial += 1
print()
print("Fin de cuenta.")








