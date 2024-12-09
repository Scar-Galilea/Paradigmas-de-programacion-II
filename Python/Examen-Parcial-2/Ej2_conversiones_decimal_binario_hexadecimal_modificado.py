#Galilea Peralta Contreras.
#07 de diciembre del 2024.
#Descripción:
#Este programa permite convertir números entre las bases decimales, binarias y hexadecimales.
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
    print("4) Suma de dos binarios.")
    print()

    #Solicita la opción del usuario.
    Opcion = int(input("Ingrese la opción: "))
    return Opcion

#Función para convertir de decimal a binario y hexadecimal.
def Decimal_a_binario_y_hexadecimal(Decimal):
    #Llama a funciones específicas para convertir decimal a binario y hexadecimal.
    Tupla_b_h = (decimal_a_binario(Decimal),decimal_a_hexadecimal(Decimal))
    return Tupla_b_h

#Función para convertir de binario a decimal y hexadecimal.
def Binario_a_decimal_y_hexadecimal(Binario):
    Binario = str(Binario) #Convierte el número a cadena para recorrerlo fácilmente.
    Acumulador_decimal = 0 #Inicializa el acumulador para almacenar el resultado decimal.

    #Convierte de binario a decimal.
    Total = (len(Binario)) - 1
    for i in Binario:
        #Suma el valor del dígito multiplicado por 2 elevado a su posición.
        Acumulador_decimal = (2 ** Total ) * int(i) + Acumulador_decimal
        Total -= 1
    Tupla_d_h = (Acumulador_decimal,decimal_a_hexadecimal(Acumulador_decimal))
    return Tupla_d_h

#Función para convertir de hexadecimal a decimal y binario.
def Hexadecimal_a_decimal_y_binario(Hexadecimal):
    Hexadecimal = str(Hexadecimal) #Convierte el número a cadena para recorrerlo.
    Acumulador_decimal = 0
    print(Hexadecimal)

    # Convierte de hexadecimal a decimal.
    Total = (len(Hexadecimal)) - 1
    for i in Hexadecimal:
        #Suma el valor del dígito multiplicado por 16 elevado a su posición.
        Acumulador_decimal = (16 ** Total) * int(Convertir_hexadecimal_a_numero(i)) + Acumulador_decimal
        Total -= 1

    Tupla_d_b = Acumulador_decimal,decimal_a_binario(Acumulador_decimal)

    return Tupla_d_b

def Convertidor_hexadecimal(Numero):
    Numero = str(Numero)
    Diccionario_hexadecimal = {('1'): '1',
                               ('2'): '2',
                               ('3'): '3',
                               ('4'): '4',
                               ('5'): '5',
                               ('6'): '6',
                               ('7'): '7',
                               ('8'): '8',
                               ('9'): '9',
                               ('10'): 'A',
                               ('11'): 'B',
                               ('12'): 'C',
                               ('13'): 'D',
                               ('14'): 'E',
                               ('15'): 'F',
                                ('0'): '0'}

    Numero = str(Diccionario_hexadecimal.get(Numero))
    return Numero
#Función para convertir caracteres hexadecimales a sus valores numéricos.
def  Convertir_hexadecimal_a_numero(Numero):
    Numero = str(Numero)
    Diccionario_hexadecimal = {('1'): '1',
                               ('2'): '2',
                               ('3'): '3',
                               ('4'): '4',
                               ('5'): '5',
                               ('6'): '6',
                               ('7'): '7',
                               ('8'): '8',
                               ('9'): '9',
                               ('A'): '10',
                               ('B'): '11',
                               ('C'): '12',
                               ('D'): '13',
                               ('E'): '14',
                               ('F'): '15',
                               ('0'): '0'}

    Numero = str(Diccionario_hexadecimal.get(Numero))
    return Numero

#Función para convertir de decimal a hexadecimal.
def decimal_a_hexadecimal(Numero_h):
    Acumulador_hexadecimal = ""

    while Numero_h // 16 != 0:
        Convertidor = Convertidor_hexadecimal((Numero_h % 16))
        Acumulador_hexadecimal = Convertidor + Acumulador_hexadecimal
        Numero_h = Numero_h // 16

    Convertidor = Convertidor_hexadecimal(Numero_h)
    return Convertidor + Acumulador_hexadecimal

#Función para convertir de decimal a binario.
def decimal_a_binario(Numero_b):
    Acumulador_binario = ""
    while Numero_b // 2 != 0:
        Acumulador_binario = str(Numero_b % 2) + Acumulador_binario
        Numero_b = Numero_b // 2
    return str(Numero_b) + Acumulador_binario

def Suma_de_binarios(Numero_1,Numero_2):
    Suma = Binario_a_decimal(Numero_1) + Binario_a_decimal(Numero_2)
    Suma_binaria = decimal_a_binario(Suma)

    return Suma_binaria



def Binario_a_decimal(Numero_1):
    Acumulador_decimal_1 = 0  # Inicializa el acumulador para almacenar el resultado decimal.
    # Convierte de binario a decimal.
    Total_1 = (len(Numero_1)) - 1
    for i in Numero_1:
        # Suma el valor del dígito multiplicado por 2 elevado a su posición.
        Acumulador_decimal_1 = (2 ** Total_1) * int(i) + Acumulador_decimal_1
        Total_1 -= 1

    return Acumulador_decimal_1


Opcion = None

while Opcion != 0:
    print()
    Opcion = Menu() #Muestra el menú y obtiene la opción del usuario.
    if Opcion == 0: #Salir del programa.
        print("Fin del programa.")
    elif Opcion == 1: #Decimal a binario y hexadecimal.
        Decimal = int(input("Ingrese el número en base decimal: "))
        Binario,Hexadecimal = Decimal_a_binario_y_hexadecimal(Decimal)
        print(f"El número decimal {Decimal} es Ob{Binario} en binario y Ox{Hexadecimal} es hexadecimal.")

    elif Opcion  == 2: #Binario a decimal y hexadecimal.
        Binario = int(input("Ingrese el número en base binaria: "))
        Decimal, Hexadecimal = Binario_a_decimal_y_hexadecimal(Binario)
        print(f"El número binario Ob{Binario} es {Decimal} en decimal y Ox{Hexadecimal} es hexadecimal.")

    elif Opcion == 3: #Hexadecimal a decimal y binario.
        Hexadecimal = input("Ingrese el número en base binaria: ")
        Decimal, Binario = Hexadecimal_a_decimal_y_binario(Hexadecimal)
        print(f"El número hexadecimal Ox{Hexadecimal} es {Decimal} en decimal y Ob{Binario} binario.")
    elif Opcion == 4:
        Binario_1 = input("Ingrese un número en base binaria: ")
        Binario_2 = input("Ingrese otro número en base binaria: ")

        suma = Suma_de_binarios(Binario_1,Binario_2)
        print(f"La suma de Ob{Binario_1} y Ob{Binario_2} es: Ob{suma}.")

    else:
        print("Opción incorrecta.") #Mensaje para opciones no válidas.
    print("______________________________________________________")
    print()