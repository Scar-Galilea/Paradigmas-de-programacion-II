#Galilea Peralta Contreras.
#26 de enero del 2025.
#Descripción:

def menu() -> int:
    print("***  Promedio ***")
    print("0) Salir.")
    print("1) Mostrar alumnos.")
    print("2) Agregar alumnos.")
    print()
    opcion = input("Elije una opción: ")

    while not opcion.isnumeric() or not (opcion == '0' or opcion == '1' or opcion == '2'):
        print("Opción invalida")
        print("___________________________________________________________________")
        print()
        opcion = input("Intenta nuevamente: ")
        print()
    return int(opcion)



if __name__ == '__main__':
    opcion = None

    while opcion != 0:
        opcion = menu()
        if opcion == 0:
            print("Fin del programa.")
        elif opcion == 1:
            while
        else:
            print()
    print("___________________________________________________________________")
























def alumnos (tema:str, ** kwargs):
    print(f"El tema es {tema}")

    for key,value in kwargs.items():
        print(f"Nombre: {key} prefiere: {value}")

def promedio (tema:str, ** kwargs):
    print(f"El tema es {tema}")

    for key,value in kwargs.items():
        print(f"Nombre: {key} prefiere: {value}")


if __name__ == '__main__':
    terminar_ciclo = None
    print("En este programa se  mostraran los alumnos que el usuario diga, con sus respectivas calificaciones y pormedios.")
    print("El numero de alumnos sera infinito hasta que el usuario pon la palabra 0 al inicio de cada alumno.")
    while terminar_ciclo != "0":
        Nombre
     alumnos("Alumnos", Rebeca ="Mole", Juan ="Tacos", Bryan ="Tlayudas")