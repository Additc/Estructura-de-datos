"""
Nombre: Addi Toro Chavez
Fecha: 25 de noviembre del 2024
Descripción:
Conjuntos ejercicio 1 rifa.
"""
from random import random
import random

correos=set()
contador_correos=0


def menu( ):
    print()
    print("Seleccione una opción")
    print("1: Ver correos de los participantes") # nombre y cantidad
    print("2: Agregar correo de participante")
    print("3: Eliminar correo de participante")
    print("4: Selecionar un ganador")
    print("0: Salir")
    opcion=int(input("Ingrese la opción: "))
    return opcion

def ver_correos(correos,contador_correos):
    if len(correos)==0:
        print("No hay participantes")
    else:
        print()
        print("El conjunto de correos es:")
        for correo in correos:
            print("-",correo)
        print()

def agregar_correo(correos,contador_correos):
    contador_correos =1
    correo=input(f"Ingrese correo del participante a participar: ")
    correos.add(correo)
    print(f"El correo {correo} ha sido agregado con exito!")

def eliminar_correo(correos, contador_correos):
    if len(correos)==0:
        print("No hay participantes")
    else:
        print()
        print("El conjunto de correos es:")
        for correo in correos:
            print("-", correo)
        print()
        participante=input("Ingrese el correo del participante que desea eliminar: ")
        correos.remove(participante)
        print("El correo se ha eliminado con exito!")




def selecciona_ganador(correos, contador_correos):
    if len(correos)==0:
        print("No hay participantes")
    else:
        lista_correo=list(correos)
        ganador = random.choice(lista_correo)
        print(f"El correo ganador es: {ganador} muchas felicidades!")


op = 1
while op != 0:
    opcion = menu()
    if opcion == 1:
        ver_correos(correos, contador_correos)
    elif opcion == 2:
        agregar_correo(correos,contador_correos)
        contador_correos += 1
    elif opcion == 3:
        eliminar_correo(correos, contador_correos)
    elif opcion == 4:
        selecciona_ganador(correos, contador_correos)
    elif opcion == 0:
        op = 0
        print("Salió del programa")
    else:
        print("opción incorrecta")
"""
Importamos la librería random y declaramos un conjunto vacío que almacenará los correos de los participantes, además de un contador.
Posteriormente defino mis funciones para cada una de las opciones, como lo son el menú, ver correos, agregar correos, eliminar correos y seleccionar un ganador.
Se implementa la lógica necesaria necesaria dentro de cada una de las funciones, peculiarmente en seleccionar un ganador donde hacemos la conversión del conjunto a una lista ,
para poder obtener un ganador.

Declaró la condición while que estará ejecutando las opciones seleccionadas por el usuario, establecidas dentro de las correspondientes condiciones.  
"""