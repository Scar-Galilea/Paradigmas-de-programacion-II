#Galilea Peralta Contreras.
#26 de enero del 2025.
#Descripción:

#Galilea Peralta Contreras.
#26 de enero del 2025.
#Descripción:

def menu() -> int:
    print("***   Ejercicio 1. Calculadora con argumentos variables ***")
    print("0) Salir.")
    print("1) Sumar todos los números ingresados.")
    print("2) Multiplicar todos los números ingresados.")
    print()
    opcion = input("Elije una opción: ")

    while not opcion.isnumeric() or not (opcion == '0' or opcion == '1' or opcion == '2'):
        print("Opción invalida")
        print("___________________________________________________________________")
        print()
        opcion = input("Intenta nuevamente: ")
        print()
    return int(opcion)

def cadena_a_flotante (cadena):
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".","")
    if revisar_cadena.isnumeric() and no_guiones in(0,1) and no_puntos in(0,1) :
        return  float(cadena)
    else:
        return None

def sumar(* vargs) -> int :
    resultado = 0
    for i in vargs:
         resultado += i
    return resultado

"""
    res = sumar(5, 3, 4)
    print(res )
"""


if __name__ == '__main__':
    opcion = None

    while opcion != 0:
        opcion = menu()
        if opcion == 0:
            print("Fin del programa.")
        elif opcion == 1:


        else:
            print()
    print("___________________________________________________________________")


"""
def sumar(* vargs) -> int :
    resultado = 0
    for i in vargs:
         resultado += i
    return resultado

    res = sumar(5, 3, 4)
    print(res )
"""

