# Galilea Peralta Contreras.
# 26 de enero del 2025.
# Descripción: Programa para jugar al ahorcado.
from random import choice


def menu() -> int:
    """
    Muestra el menú del programa.
    :return: Un número entero que representa la opción seleccionada (0 o 1).
    """
    print("***  Ahorcado  ***")
    print("0) Salir.")
    print("1) Jugar")
    print()
    opcion = input("Elige una opción: ")  #La opción ingresada por el usuario

    while not opcion.isnumeric() or not (opcion == '0' or opcion == '1'):
        print("Opción inválida.")
        print("___________________________________________________________________")
        print()
        opcion = input("Intenta nuevamente: ")  # Nueva entrada si la anterior fue inválida
        print()
    return int(opcion)

def palabras() -> str:
    lista_de_palabras = []
    lista_de_palabras.append("hola")
    lista_de_palabras.append("oso")
    lista_de_palabras.append("historia")
    lista_de_palabras.append("filosofia")
    lista_de_palabras.append("electronica")
    lista_de_palabras.append("gato")

    eleccion = choice(lista_de_palabras)
    return eleccion



def jugar():
    """
    Ejecuta el juego del ahorcado.
    Permite al usuario adivinar una palabra letra por letra hasta que se quede sin intentos o gane.
    """
    lista_de_las_letras = []  #Lista que almacena las letras adivinadas correctamente.
    intentos = 0  #Contador de intentos del jugador.
    bandera = 0  #Indica si la palabra ha sido adivinada
    palabra = palabras().lower()  #Palabra secreta a adivinar.
    print()
    print("Comienza el juego.")
    intentos = len(palabra) + 2
    print(f"Tienes {intentos} intentos.")
    print()

    for _ in range(len(palabra)):
        lista_de_las_letras.append('_')  #Inicializa la lista con guiones bajos.
    numero = 0
    while (numero < intentos and bandera == 0):
        print()
        verificador = 0  #Verifica si todas las letras han sido adivinadas.
        contador = 0  #Índice para recorrer la palabra.
        prueba = 0  #Controla la validación de la letra ingresada.

        for i in range(len(palabra)):
            print(lista_de_las_letras[i], end=" ")
        print()

        print(f"Oportunidad {intentos}")
        letra = input("Escoja una letra: ").lower()  #Letra ingresada por el usuario.

        if len(letra) > 1:
            prueba = 2

        while prueba >= 2:
            prueba = 0
            print("Solo se puede ingresar una letra.")
            letra = input("Intenta de nuevo: ").lower()  #Nueva entrada si la anterior no es válida.
            if len(letra) > 1:
                prueba = 2

        for m in palabra:
            if m == letra:
                lista_de_las_letras[contador] = letra  #Actualiza la lista con la letra correcta.
            contador += 1

        for m in palabra:
            if m != lista_de_las_letras[verificador]:
                bandera = 0
            else:
                bandera = 1
            verificador += 1

        intentos -= 1

    print()
    if bandera == 1:
        print("¡Felicidades, ganaste!")
        for i in range(len(palabra)):
            print(lista_de_las_letras[i], end=" ")
        print()
    else:
        print("Lo siento, perdiste.")
        print(f"La palabra era: {palabra}.")

if __name__ == '__main__':
    """
    Punto de entrada principal del programa.
    Permite al usuario seleccionar entre jugar o salir.
    """
    opcion = None  # Almacena la opción del usuario.

    while opcion != 0:
        opcion = menu()
        if opcion == 0:
            print("Fin del programa.")
        elif opcion == 1:
            jugar()
        else:
            print()
    print("________________________________")
