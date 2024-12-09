#Galilea Peralta Contreras.
#07 de diciembre del 2024.
#Descripción:

"""
Instrucciones:
Escribe un programa de nombre Ej2_conversiones_decimal_binario_hexadecimal.py que realice lo que se indica en la descripción del programa.
Comparte el enlace de GitHub en la caja de texto al final de la pregunta.

Descripción del programa:
Este programa convierte números entre las bases decimal, binaria y hexadecimal.
Se debe mostrar el siguiente menú:

  ***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***
1) Convertir de decimal a binario y hexadecimal.
2) Convertir de binario a decimal y hexadecimal.
3) Convertir de hexadecimal a decimal y binario.
0) Salir.

Cualquier otro caso -> Opción no válida.
Para ello:
a) Utilice la lógica adecuada para mostrar las conversiones. No utilice funciones como bin() o hex().
b) Asuma que el usuario siempre va a ingresar números en el formato adecuado. Por ejemplo: 1001 como número binario o 1F como hexadecimal, no 120 como número binario o 1Z como hexadecimal.
c) Para considerar el ejercicio como completo, utilice funciones para mostrar el menú y para las conversiones entre bases, considerando que cada función devuelve una tupla. Por ejemplo, la función que recibe el número decimal debe devolver el valor en binario y en hexadecimal como una tupla.
"""


#Función para mostrar el menú y devolver la opción seleccionada.
def Menu():
    print("***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***")
    print()
    print("0) Salir.")
    print("1) Convertir de decimal a binario y hexadecimal.")
    print("2) Convertir de binario a decimal y hexadecimal.")
    print("3) Convertir de hexadecimal a decimal y binario.")
    print()

    #Solicita la opción del usuario.
    Opcion = int(input("Ingrese la opción: "))
    return Opcion

def Decimal_a_binario_y_hexadecimal(Decimal):


    Numero_b = Decimal
    Numero_h = Decimal
    Acumulador_binario = ""
    Acumulador_hexadecimal = ""
    Tupla_b_h = (1,2)
    while Numero_b // 2 != 0:
        Acumulador_binario = str(Numero_b % 2) + Acumulador_binario
        Numero_b = Numero_b // 2

    while Numero_h // 16 != 0:
        Acumulador_hexadecimal = str(Numero_h % 16) + Acumulador_hexadecimal
        Numero_h = Numero_h // 16



    print(str(Numero_b)+Acumulador_binario)
    print(str(Numero_h) + Acumulador_hexadecimal)

    return Tupla_b_h

def Binario_a_decimal_y_hexadecimal(Binario):
    Tupla_d_h = (1,2)
    return Tupla_d_h
def Hexadecimal_a_decimal_y_binario(Hexadecimal):
    Tupla_d_b = (1,2)
    return Tupla_d_b



Opcion = None
Diccionario_hexadecimal = {('1'):'1',
                           ('2'):'2',
                           ('3'):'3',
                           ('4'):'4',
                           ('5'):'5',
                           ('6'):'6',
                           ('7'):'7',
                           ('8'):'8',
                           ('9'):'9',
                           ('10'):'A',
                           ('11'):'B',
                           ('12'):'C',
                           ('13'):'D',
                           ('14'):'E',
                           ('15'):'F'}

while Opcion != 0:
    print()
    Opcion = Menu() #Muestra el menú y obtiene la opción del usuario.
    if Opcion == 0: #Salir del programa.
        print("Fin del programa.")
    elif Opcion == 1:
        Decimal = int(input("Ingrese el número en base decimal: "))
        Binario,Hexadecimal = Decimal_a_binario_y_hexadecimal(Decimal)
    elif Opcion  == 2:
        Binario = int(input("Ingrese el número en base binaria: "))
        Decimal, Hexadecimal = Binario_a_decimal_y_hexadecimal(Binario)
    elif Opcion == 3:
        Hexadecimal = int(input("Ingrese el número en base binaria: "))
        Decimal, Binaria = Hexadecimal_a_decimal_y_binario(Hexadecimal)

    else:
        print()
        print("Opción incorrecta.") #Mensaje para opciones no válidas.
    print("______________________________________________________")
    print()