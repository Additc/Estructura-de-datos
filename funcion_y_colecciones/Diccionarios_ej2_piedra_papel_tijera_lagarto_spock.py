"""
Nombre: Addi Toro Chavez
Fecha: 4 de diciembre del 2024
Descripción:
Diccionarios ejercicio 1 piedra, papel, tijera , lagarto spook.
"""
from random import choice # Importó la librería random

#De claro los contadores que llevarán el conteo del juego
contador_jugador=0
contador_cpu=0
contador_empate=0

#Defino la función del menú principal con sus respectivas opciones
def menu():
    print()
    print("** Juego de piedra, papel, tijera, lagarto, spock **")
    print("Ingrese una opción para comenzar con el juego:")
    print("1) Piedra")
    print("2) Papel")
    print("3) Tijera")
    print("4) Lagarto")
    print("5) Spock")
    print("6) Ver reglas")
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
    elif opcion == 4:
        eleccion_usuario = "LAGARTO"
    elif opcion == 5:
        eleccion_usuario = "SPOCK"
    eleccion_cpu=choice(["PIEDRA","PAPEL","TIJERA","LAGARTO","SPOCK"])
    return eleccion_usuario,eleccion_cpu

def reglas():
    print()
    print("**Reglas del juego**")
    print("Seleccione una de las opciones de acuerdo a lo siguiente : ")
    print("1._Tijera corta papel")
    print("2._Papel cubre roca")
    print("3._Roca tritura lagarto")
    print("4._lagarto envenena spock")
    print("5._Spock aplasta tijera")
    print("6._Tijeras decapita lagarto")
    print("7._Lagarto come papel")
    print("8._Papel deaprueba spock")
    print("9._Spock vaporiza roca")
    print("10._Roca tritura tijeras")
    print("La CPU va elegir una de las opciones de manera aleatoria.")

#Declaro un ciclo (while) que estará repitiendose mientras el usuario elija la opción que desee.
op=1
while op != 0:
    opcion = menu()
    if opcion==1 :
        jugador(opcion)
    elif opcion == 2:
        jugador(opcion)
    elif opcion == 3:
        jugador(opcion)
    elif opcion == 4:
        jugador(opcion)
    elif opcion == 5:
        jugador(opcion)
    elif opcion == 6:
        reglas()
        opcion=menu()
    elif opcion == 0:
        print("El juego terminó")
        break
    else:
        print("opcion incorrecta")
    #Se define el diccionario, que establece la lógica del juego, implementando las nuevas restricciones.
    piedra_papel_tijeras={('PIEDRA','TIJERA'):"JUGADOR",
                            ('PIEDRA','PAPEL'):"CPU",
                            ('TIJERA','PAPEL'):"JUGADOR",
                            ('TIJERA','PIEDRA'):"CPU",
                            ('PAPEL','PIEDRA'):"JUGADOR",
                            ('PAPEL','TIJERA'):"CPU",
                            ('PIEDRA','LAGARTO'):"JUGADOR",
                            ('LAGARTO','PIEDRA'):"CPU",
                            ('LAGARTO','SPOCK'):"JUGADOR",
                            ('SPOCK','LAGARTO'):"CPU",
                            ('SPOCK','TIJERA'):"JUGADOR",
                            ('TIJERA','SPOCK'):"CPU",
                            ('TIJERA','LAGARTO'):"JUGADOR",
                            ('LAGARTO','TIJERA'):"CPU",
                            ('LAGARTO', 'PAPEL'): "JUGADOR",
                            ('PAPEL', 'LAGARTO'): "CPU",
                            ('PAPEL', 'SPOCK'): "JUGADOR",
                            ('SPOCK', 'PAPEL'): "CPU",
                            ('SPOCK', 'PIEDRA'): "JUGADOR",
                            ('PIEDRA', 'SPOCK'): "CPU"}
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
        #Muestro los resultados acumulados
        print(f"Victorias del jugador:{contador_jugador}. Victorias del CPU: {contador_cpu}. Empates:{contador_empate}")
    elif resultado == "CPU":
        # Gana el CPU e incremento su contador
        contador_cpu += 1
        # Muestro en pantalla los resultados del juego
        print(f"Jugador: {eleccion_usuario}, CPU: {eleccion_cpu}. El resultado es: {resultado}")
        # Muestro los resultados acumulados
        print(f"Victorias del jugador:{contador_jugador}. Victorias del CPU: {contador_cpu}. Empates:{contador_empate}")
    elif resultado == "EMPATE":
        # El reultado es empate e incremento su contador
        contador_empate+= 1
        # Muestro en pantalla los resultados del juego
        print(f"Jugador: {eleccion_usuario}, CPU: {eleccion_cpu}. El resultado es: {resultado}")
        # Muestro los resultados acumulados
        print(f"Victorias del jugador:{contador_jugador}. Victorias del CPU: {contador_cpu}. Empates:{contador_empate}")
