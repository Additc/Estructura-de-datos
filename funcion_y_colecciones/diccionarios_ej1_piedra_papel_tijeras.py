"""
Nombre: Addi Toro Chavez
Fecha: 4 de diciembre del 2024
Descripción:
Diccionarios ejercicio 1 piedra, papel, tijera.
"""
from random import choice # Importó la librería random

#De claro los contadores que llevarán el conteo del juego
contador_jugador=0
contador_cpu=0
contador_empate=0

#Defino la función del menú principal con sus respectivas opciones
def menu():
    print()
    print("**Juego de piedra, papel y tijera**")
    print("Ingrese una opción para comenzar con el juego:")
    print("1) Piedra")
    print("2) Papel")
    print("3) Tijera")
    print("0) Salir")
    opcion=int(input("Ingrese una opción: "))
    return opcion

#Defino la función de las opciones del usuario y del cpu
def jugador (opcion):
    if opcion == 1:
        eleccion_usuario = "PIEDRA"
    elif opcion == 2:
        eleccion_usuario="PAPEL"
    elif opcion == 3:
        eleccion_usuario = "TIJERA"
    eleccion_cpu=choice(["PIEDRA","PAPEL","TIJERA"])
    return eleccion_usuario,eleccion_cpu

#Declaro un ciclo (while) que estará repitiendose mientras el usuario elija la opción que desee
op=1
while op != 0:
    opcion = menu()
    if opcion < 0 or opcion > 3:
        print("Opción no válida")
        print()
        opcion=menu()
    if opcion == 0:
        print("El juego terminó")
        break
    #Se define el diccionario, que establece la lógica del juego.
    piedra_papel_tijeras={('PIEDRA','TIJERA'):"JUGADOR",
                         ('PIEDRA','PAPEL'):"CPU",
                         ('TIJERA','PAPEL'):"JUGADOR",
                         ('TIJERA','PIEDRA'):"CPU",
                         ('PAPEL','PIEDRA'):"JUGADOR",
                         ('PAPEL','TIJERA'):"CPU"}
    #Se obtiene la elección del jugador, y del CPU
    eleccion_usuario, eleccion_cpu = jugador(opcion)

    #Se obtiene el resultado
    resultado=piedra_papel_tijeras.get((eleccion_usuario,eleccion_cpu),'EMPATE')

    #Se establecen las condiciones, comparando el resultado
    if resultado == "JUGADOR":
        #Gana el jugador e incremento su contador
        contador_jugador+=1
        #Muestro en pantalla los resultados del juego
        print(f"Jugador: {eleccion_usuario}, CPU: {eleccion_cpu}. El resultado es: {resultado}")
        print("Gana el jugador")
        #Muestro los resultados acumulados
        print(f"Victorias del jugador:{contador_jugador}. Victorias del CPU: {contador_cpu}. Empates:{contador_empate}")
    elif resultado == "CPU":
        # Gana el CPU e incremento su contador
        contador_cpu += 1
        # Muestro en pantalla los resultados del juego
        print(f"Jugador: {eleccion_usuario}, CPU: {eleccion_cpu}. El resultado es: {resultado}")
        print("Gana el CPU")
        # Muestro los resultados acumulados
        print(f"Victorias del jugador:{contador_jugador}. Victorias del CPU: {contador_cpu}. Empates:{contador_empate}")
    elif resultado == "EMPATE":
        # El reultado es empate e incremento su contador
        contador_empate+= 1
        # Muestro en pantalla los resultados del juego
        print(f"Jugador: {eleccion_usuario}, CPU: {eleccion_cpu}. El resultado es: {resultado}")
        print("Empate")
        # Muestro los resultados acumulados
        print(f"Victorias del jugador:{contador_jugador}. Victorias del CPU: {contador_cpu}. Empates:{contador_empate}")

