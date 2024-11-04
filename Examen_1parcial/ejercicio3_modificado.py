'''
Nombre: Addi Toro Chavez
Fecha: 27 de octubre de 2024.
Descripción:
Este programa es el famoso juego de "piedra, papel o tijera", en donde el contrincante es la CPU. La opción de la CPU se escogerá de forma aleatorio con la función randint().

El juego mostrará las victorias del jugador, los partidos empatados y las victorias del CPU. Además, mostrará el siguiente menú:

    1) Piedra.
    2) Papel.
    3) Tijera.
    0) Salir.
    Cualquier otro caso -> Mostrar un mensaje de "opción no válida".

Para ello:
a) Muestre la cantidad de victorias, empates y derrotas.
b) Pida al usuario una opción del menú.
c) Realice la lógica adecuada para calcular al ganador.
d) Muestre en la consola la elección del jugador, del CPU y el resultado.
e) Repita nuevamente el menú hasta salir.
'''
# Importamos la librería random.
from random import randint
import random
# Declaro los contadores y los inicializo según el caso.
opcion = 1
victorias_jugador = 0
partidos_empatados = 0
victorias_cpu = 0

# Muestro en pantalla las opciones para desarrollar el juego y así mismo las veces que ah ganado, empatado y perdido.
while opcion != 0:
    print(f"Victoria del jugador: {victorias_jugador}, juegos empatados: {partidos_empatados}, victorias del cpu: {victorias_cpu}")
    print()
    print("Ingrese una opción: ")
    print("1) Piedra")
    print("2) Papel")
    print("3) Tijera")
    print("0) Salir")
    opcion=input("Ingrese de la opcion que desea (piedra,papel o tijera): ") # El usuario ingresa la opción que desea.
    opcion = opcion.lower()
#La computadora genera un número aleatorio entre 1 y 3.
    CPU_op= randint(1,3)

# De acuerdo al número que la computadora generé le asigno a una variable una cadena, según corresponda.
    if CPU_op == 1:
        CPU ="piedra"
    elif CPU_op == 2:
        CPU = "papel"
    else:
        CPU = "tijera"
    # De igual manera hago lo mismo de asignar una cadena a una variable según sea la opción del usuario.
    if opcion == "piedra"or opcion == "papel" or opcion == "tijera":
        if CPU == opcion:
            partidos_empatados +=1
            print(f"Jugador: {opcion}")
            print(f"CPU: {CPU}")
            print("El resultado es empate.")
            print()
        elif (CPU_op == 1 and opcion == "tijera") or (CPU_op == 3 and opcion == "papel") or (CPU_op == 2 and opcion == "piedra"):
            victorias_jugador +=1
            print(f"Jugador: {opcion}")
            print(f"CPU: {CPU}")
            print("Gana jugador")
            print()
        elif (opcion == "piedra" and CPU_op == 3) or (opcion == "tijera" and CPU_op == 2) or (opcion == "papel" and CPU_op == 1):
            victorias_cpu += 1
            print(f"Jugador: {opcion}")
            print(f"CPU: {CPU}")
            print("Gana CPU")
            print()
    elif opcion == 0:
        opcion = 0
        print("Salió del programa") # Salgo del programa
    else:
         print("opcion incorrecta, ingrese de nuevo.")
         print()