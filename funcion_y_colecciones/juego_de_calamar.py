'''
Nombre: Addi Toro Chavez
Fecha: 27 de octubre de 2024.
Descripción:
Este programa es el famoso juego de "piedra, papel o tijera -1", en donde el contrincante es la CPU.

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
    opcion=int(input("Ingrese el número de la primera opción que desea: ")) # El usuario ingresa la opción que desea.
    opcion2 = int(input("Ingrese el número de la segunda opción que desea: "))
#La computadora genera un número aleatorio entre 1 y 3.
    CPU_op= randint(1,3)
    CPU_op2=randint(1,3)

# De acuerdo al número que la computadora generé le asigno a una variable una cadena, según corresponda.
    if CPU_op == 1:
        CPU ="Piedra"
    elif CPU_op == 2:
        CPU = "Papel"
    else:
        CPU = "Tijera"

    if CPU_op2== 1:
        CPU2="Piedra"
    elif CPU_op2== 2:
        CPU2 = "Papel"
    else:
        CPU2 = "Tijera"
# De igual manera hago lo mismo de asignar una cadena a una variable según sea la opción del usuario.
    if opcion == 1:
        player_op1 = "Piedra"
    elif opcion == 2:
        player_op1 = "Papel"
    else:
         player_op1 = "Tijera"

    if opcion2 == 1:
        player_op2 = "Piedra"
    elif opcion2 == 2:
        player_op2 = "Papel"
    else:
         player_op2 = "Tijera"

    print()
    print(f"El usuario elige: {player_op1} y {player_op2}")
    print(f"La CPU elige: {CPU} y {CPU2}")
    print()
    print("Ahora solo seleccione una opción para continuar con el juego:")
    opcion_final=input(f"Ingrese su elección final {player_op1} o {player_op2}: ")
    opcion_final.lower()
    if opcion_final == "piedra":
        player = "Piedra"
    elif opcion_final == "papel":
        player = "Papel"
    elif opcion_final == "tijera":
        player = "Tijera"
    else:
        print("Acción incorrecta")

    cpu_final=randint(CPU_op,CPU_op2)
    if cpu_final == 1:
        CPU3 ="Piedra"
    elif cpu_final == 2:
        CPU3 = "Papel"
    else:
        CPU3 = "Tijera"
    print("cpu fonal: ", CPU3)

# Realizo la lógica con las distintas condiciones y comparaciones para determinar al ganador y si en dado caso empataron.
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