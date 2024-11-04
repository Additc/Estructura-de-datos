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
    opcion=int(input("Ingrese el número de la opcion que desea: ")) # El usuario ingresa la opción que desea.

#La computadora genera un número aleatorio entre 1 y 3.
    CPU_op= randint(1,3)

# De acuerdo al número que la computadora generé le asigno a una variable una cadena, según corresponda.
    if CPU_op == 1:
        CPU ="Piedra"
    elif CPU_op == 2:
        CPU = "Papel"
    else:
        CPU = "Tijera"
# De igual manera hago lo mismo de asignar una cadena a una variable según sea la opción del usuario.
    if opcion == 1:
        player = "Piedra"
    elif opcion == 2:
        player = "Papel"
    else:
         player = "Tijera"

# Realizo la lógica con las distintas condiciones y comparaciones para determinar al ganador y si en dado caso empataron
    if CPU_op == opcion:
        partidos_empatados +=1
        print(f"Jugador: {player}, CPU: {CPU}, el resultado es empate.")
        print()
    elif (CPU_op == 1 and opcion == 2) or (CPU_op == 2 and opcion == 3) or (CPU_op == 3 and opcion == 1):
        victorias_jugador +=1
        print(f"Jugador: {player}, CPU: {CPU}, ganador el jugador.")
        print()
    elif (opcion == 1 and CPU_op == 2) or (opcion == 2 and CPU_op == 3) or (opcion == 3 and CPU_op == 1):
        victorias_cpu += 1
        print(f"Jugador: {player}, CPU: {CPU}, Gana el CPU.")
        print()
    elif opcion == 0:
        opcion = 0
        print("Salió del programa") # Salgo del programa
    else:
        print("opcion incorrecta")