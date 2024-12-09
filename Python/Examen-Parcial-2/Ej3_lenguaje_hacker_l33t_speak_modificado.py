#Galilea Peralta Contreras.
#07 de diciembre del 2024.
#Descripción:
#Este programa convierte un texto al lenguaje hacker (l33t sp34k) en dos niveles:
#1. Lenguaje básico: Convierte solo las vocales.
#2. Lenguaje intermedio: Convierte tanto vocales como consonantes utilizando el alfabeto hacker.

"""
Instrucciones:
Escribe un programa de nombre Ej3_lenguaje_hacker_l33t_speak.py que realice lo que se indica en la descripción del programa.
Comparte el enlace de GitHub en la caja de texto al final de la pregunta.

Descripción del programa:
Este programa convierte un texto al lenguaje hacker (lenguaje leet o 1337). Esta escritura se caracteriza por reemplazar las letras por números y símbolos.
Revisa la siguiente página para mayor información: https://www.gamehouse.com/blog/leet-speak-cheat-sheet/

Lenguaje básico:
En el lenguaje básico se sustituye cada vocal por un número.
La A se convierte en un 4, la E en un 3, la I en un 1 y la O en un cero.
La letra U es una excepción, ya que no hay un número obvio, por lo que se sustituye por (_).

Lenguaje intermedio:
En el lenguaje intermedio también se sustituyen las consonantes por números o signos de puntuación.
Por ejemplo, la B se convierte en I3, la C en [, la D en ), la L en 1.
Revisa la "Leet speak alphabet" de la página anterior y toma la primera de las opciones para el lenguaje.
Nota que no hay caracteres acentuados, por lo no se deben de convertir.

Se debe mostrar el siguiente menú:
  ***  Ejercicio 3. Lenguaje hacker (l33t sp34k).  ***
1) Convertir un texto a lenguaje básico.
2) Convertir un texto a lenguaje intermedio.
0) Salir.
Cualquier otro caso -> Opción no válida.

Para ello:
a) Utilice la lógica adecuada para mostrar las conversiones. No utilice funciones como bin() o hex().
a) Utilice la lógica adecuada para convertir el texto al lenguaje hacker básico o intermedio, según sea el caso.
b) Se debe convertir los caracteres sin importar si son mayúsculas o minúsculas, sin modificar los caracteres que no se convirtieron. Ejemplos con el lenguaje básico: hola -> h0l4, Hola -> H0l4, HOLA -> H0L4.
"""

#Función para mostrar el menú y devolver la opción seleccionada.
def Menu():
    print("***  Ejercicio 3. Lenguaje hacker (l33t sp34k).  ***")
    print()
    print("0) Salir.")
    print("1) Convertir un texto a lenguaje básico.")
    print("2) Convertir un texto a lenguaje intermedio.")
    print()

    #Solicita la opción del usuario.
    Opcion = int(input("Ingrese la opción: "))
    return Opcion


Opcion = None

#Diccionario para convertir vocales al lenguaje básico (solo vocales).
Diccionario_de_vocales = {('a'): '4',
                          ('e'): '3',
                          ('i'): '1',
                          ('o'): '0',
                          ('u'): '(_)',
                          ('0'): 'o',
                          ('1'): 'L',
                          ('2'): 'R',
                          ('3'): 'E',
                          ('4'): 'A',
                          ('5'): 'S',
                          ('6'): 'b',
                          ('7'): 'T',
                          ('8'): 'B',
                          ('9'): 'g' }



#Diccionario para convertir tanto vocales como consonantes al lenguaje intermedio.
Diccionario_de_completo = {('a'): '4',
                          ('b'): 'l3',
                          ('c'): '[',
                          ('d'): ')',
                          ('e'): '3',
                          ('f'): '|=',
                          ('g'): '&',
                          ('h'): '#',
                          ('i'): '1',
                          ('j'): ',_|',
                          ('k'): '>|',
                          ('l'): '1',
                          ('m'): '/\/\ ',
                          ('n'): '^/',
                          ('o'): '0',
                          ('p'): '|*',
                          ('q'): '(_.)',
                          ('r'): 'l2',
                          ('s'): '5',
                          ('t'): '7',
                          ('u'): '(_)',
                          ('v'): '\/',
                          ('w'): '\/\/',
                          ('x'): '><',
                          ('y'): 'j',
                          ('z'): '2',
                          ('0'): 'o',
                          ('1'): 'L',
                          ('2'): 'R',
                          ('3'): 'E',
                          ('4'): 'A',
                          ('5'): 'S',
                          ('6'): 'b',
                          ('7'): 'T',
                          ('8'): 'B',
                          ('9'): 'g' }

#Ciclo principal para ejecutar el programa hasta que el usuario decida salir
while Opcion != 0:
    Opcion = Menu() #Muestra el menú y obtiene la opción del usuario.
    if Opcion == 0: #Salir del programa.

        print("Fin del programa.")
    elif Opcion == 1: #Conversión al lenguaje básico (solo vocales).
        Texto = input("Ingresa el texto a convertir a lenguaje l33t sp34k básico: ")
        Lenguaje_basico = "" #Almacena el texto convertido.
        #Recorre cada carácter del texto ingresado.
        for t in Texto:
            #Convierte las vocales y mantiene los caracteres no modificados.
            Lenguaje_basico =Lenguaje_basico + Diccionario_de_vocales.get((t.lower()),t)
        print()
        print("El es texto convertido es: ")
        print(Lenguaje_basico)

    elif Opcion  == 2: #Conversión al lenguaje intermedio (vocales y consonantes).
        Texto = input("Ingresa el texto a convertir a lenguaje l33t sp34k básico: ")
        Lenguaje_i = "" #Almacena el texto convertido.
        #Recorre cada carácter del texto ingresado.
        for t in Texto:
            #Convierte las letras según el diccionario y mantiene caracteres no modificados.
            Lenguaje_i = Lenguaje_i + Diccionario_de_completo.get((t.lower()),t)
        print()
        print("Él es texto convertido es: ")
        print(f"{Lenguaje_i}")

    else:
        print()
        print("Opción incorrecta.") #Mensaje para opciones no válidas.
    print("______________________________________________________")
    print()