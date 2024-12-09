#Galilea Peralta Contreras.
#07 de diciembre del 2024.
#Descripción:

"""
Instrucciones:
Escribe un programa de nombre Ej4_sombrero_seleccionador.py que realice lo que se indica en la descripción del programa.
Comparte el enlace de GitHub en la caja de texto al final de la pregunta.

Descripción del programa:
Este programa es un test de la elección del sombrero seleccionador de Harry Potter para alguna de las casas: Gryffindor, Slytherin, Hufflepuff y Ravenclaw.
Ejemplos de preguntas:

¿Cuál de las siguientes opciones odiarías más que la gente te llamara?
Gryffindor - Ordinario.
Slytherin - Ignorante.
Hufflepuff - Cobarde.
Ravenclaw - Egoísta.

Después de tu muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?
Gryffindor - Te extraña, pero sonríe.
Slytherin - Pide más historias sobre tus aventuras.
Hufflepuff - Piensa con admiración tus logros.
Ravenclaw - No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta.

Dada la opción, preferirías inventar una poción que garantizara:
Gryffindor - Gloria.
Slytherin - Sabiduría.
Hufflepuff - Amor.
Ravenclaw - Poder.

¿Cómo te definirías en una sola palabra?
Gryffindor - Valiente.
Slytherin - Ambicioso.
Hufflepuff - Leal.
Ravenclaw - Curioso.

¿Qué cualidad te describe mejor?
Gryffindor - La fuerza.
Slytherin - La astucia.
Hufflepuff - La paciencia.
Ravenclaw - La inteligencia.

¿Cuál es tu clase favorita?
Gryffindor - Vuelo.
Slytherin - Defensa contra las artes oscuras.
Hufflepuff - Animales fantásticos.
Ravenclaw - Pociones.

¿Cuál es tu lenguaje de programación favorito?
Gryffindor - C.
Slytherin - Python.
Hufflepuff - C++.
Ravenclaw - JavaScript.

Se debe mostrar la siguiente pantalla inicial:
  ***  Ejercicio 4. Test del sombrero seleccionador de Harry Potter.  ***
Este programa determina la casa (Gryffindor, Slytherin, Hufflepuff y Ravenclaw) a la que perteneces, de acuerdo a tus respuestas.

1) Iniciar test.
0) Salir.
Cualquier otro caso -> Opción no válida.
Para ello:

a) Realice al menos 5 preguntas al usuario. Puede utilizar las 7 aquí presentadas.
b) El orden de las respuestas presentadas no debe ser el mismo al repetir el test. Se recomienda combinar conjuntos, listas y diccionarios para este fin.
c) Utilice la lógica adecuada para determinar la casa con base en las respuestas.
d) Muestre la casa al final del test y finalice el programa.
"""

#Función para mostrar el menú y devolver la opción seleccionada.
def Menu():
    print("***  Ejercicio 4. Test del sombrero seleccionador de Harry Potter.  ***")
    print()
    print("0) Salir.")
    print("1) Iniciar test.")
    print()

    #Solicita la opción del usuario.
    Opcion = int(input("Ingrese la opción: "))
    return Opcion


def Respuestas(Conjunto):
    R1, R2, R3, R4= Conjunto
    print(f"    1) {R1}")
    print(f"    2) {R2}")
    print(f"    3) {R3}")
    print(f"    4) {R4}")
    print()
    Respuesta = input("Selecciona tu respuesta: ")

    if Respuesta == '1':
        Respuesta = R1
    elif Respuesta == '2':
        Respuesta = R2
    elif Respuesta == '3':
        Respuesta = R3
    elif Respuesta == '4':
        Respuesta = R4
    else:
        Respuesta = '0'
        print("Opción no válida. Elige un número del 1 al 4")

    return Respuesta


Opcion = None

Gryffindor = ("Ordinario.","Te extraña, pero sonríe.","Gloria."," Valiente.","La fuerza.")
Slytherin = ("Ignorante.","Pide más historias sobre tus aventuras.","Sabiduría.","Ambicioso.","La astucia.")
Hufflepuff = ("Cobarde.","Piensa con admiración tus logros.","Amor.","Leal","La paciencia.")
Ravenclaw = ("Egoísta.","No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta.","Poder.","Curioso.","La inteligencia.")

Conjunto_1 = set()
Conjunto_2 = set()
Conjunto_3 = set()
Conjunto_4 = set()
Conjunto_5 = set()

Conjunto_1 = {Gryffindor[0],Slytherin[0],Hufflepuff[0],Ravenclaw[0]}
Conjunto_2 = {Gryffindor[1],Slytherin[1],Hufflepuff[1],Ravenclaw[1]}
Conjunto_3 = {Gryffindor[2],Slytherin[2],Hufflepuff[2],Ravenclaw[2]}
Conjunto_4 = {Gryffindor[3],Slytherin[3],Hufflepuff[3],Ravenclaw[3]}
Conjunto_5 = {Gryffindor[4],Slytherin[4],Hufflepuff[4],Ravenclaw[4]}

Respuesta = [Conjunto_1,Conjunto_2,Conjunto_3,Conjunto_4,Conjunto_5]

Preguntas = ['a) ¿Cuál de las siguientes opciones odiarías más que la gente te llamara?','Después de tu muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?','c)Dada la opción, preferirías inventar una poción que garantizara','d) ¿Cómo te definirías en una sola palabra?','c)¿Qué cualidad te describe mejor?']

Puntos_G = 0
Puntos_S = 0
Puntos_H = 0
Puntos_R = 0


while Opcion != 0:
    Opcion = Menu() #Muestra el menú y obtiene la opción del usuario.
    if Opcion == 0: #Salir del programa.

        print("Fin del programa.")
    elif Opcion == 1:
        Seleccion = ['0','0','0','0','0']

        Posicion = 0
        while Posicion < 5:
            while Seleccion[Posicion] == '0':
                print()
                print(Preguntas[Posicion])
                Seleccion.pop(Posicion)
                Seleccion.insert(Posicion, Respuestas(Respuesta[Posicion]))
            Posicion += 1



        Posicion = 0
        while Posicion < 5:
            if Seleccion[Posicion] == Gryffindor[Posicion]:
                Puntos_G += 1
            elif Seleccion[Posicion] == Slytherin[Posicion]:
                Puntos_S += 1
            elif Seleccion[Posicion] == Hufflepuff[Posicion]:
                Puntos_H += 1
            elif Seleccion[Posicion] == Ravenclaw[Posicion]:
                Puntos_R += 1
            Posicion += 1

        if Puntos_G > Puntos_S and Puntos_G > Puntos_H and Puntos_G > Puntos_R:
            print("Tu casa es: Gryffindor.")
        elif Puntos_S > Puntos_G and Puntos_S > Puntos_H and Puntos_G > Puntos_R:
            print("Tu casa es: Slytherin.")
        elif Puntos_H > Puntos_G and Puntos_H > Puntos_S and Puntos_H > Puntos_R:
            print("Tu casa es: Hufflepuff.")
        elif Puntos_R > Puntos_G and Puntos_R > Puntos_S and Puntos_R > Puntos_H:
            print("Tu casa es: Ravenclaw.")
        else:
            print("Vuelva intentar el test.")

        Opcion = 0

    else:
        print()
        print("Opción incorrecta.") #Mensaje para opciones no válidas.
    print("______________________________________________________")
    print()