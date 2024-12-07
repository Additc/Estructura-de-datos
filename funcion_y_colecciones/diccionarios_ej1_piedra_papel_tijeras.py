"""
Nombre: Addi Toro Chavez
Fecha: 4 de diciembre del 2024
Descripción:
Diccionarios ejercicio 1 piedra, papel, tijera.
"""
import random
contador_jugador=0
contador_cpu=0
contado_empate=0
diccionario_juego={'PIEDRA':"piedra",'PAPEL':"papel",'TIJERA':"tijera",'JUGADOR':"Gana el jugador",'EMPATE':"Empate",'CPU':"Gana la cpu"}

def menu():
    print()
    print("**Juego de piedra, papel y tijera**")
    print("Ingrese una opcion para empezar con el juego:")
    print("1) Piedra")
    print("2) Papel")
    print("3) Tijera")
    opcion=input("Ingrese una opcion: ")
    return opcion

def jugador (opcion, diccionario_juego):
    if opcion == 1:
        eleccion_usuario = diccionario_juego.get('PIEDRA')
    elif opcion == 2:
        eleccion_usuario = diccionario_juego.get('PAPEL')
    elif opcion == 3:
        eleccion_usuario = diccionario_juego.get('TIJERA')
    else:
        print("Accion incorrecta, intente de nuevo")
    eleccion_cpu=random.choice(['PIEDRA','PAPEL','TIJERA'])
    return eleccion_usuario,eleccion_cpu

def logica_juego(diccionario_juego,eleccion_usuario,eleccion_cpu,contador_jugador,contador_cpu,contador_empate):
    piedra_pape_tijeras={('PIEDRA','TIJERAS'):"JUGADOR",
                         ('PIEDRA','PAPEL'):"CPU",
                         ('TIJERAS','PAPEL'):"JUGADOR",
                         ('TIJERAS','PIEDRA'):"CPU",
                         ('PAPEL','PIEDRA'):"JUGADOR",
                         ('PAPEL','TIJERAS'):"CPU"}
    resultado=piedra_pape_tijeras.get((eleccion_usuario,eleccion_cpu))
    if resultado == "JUGADOR":
        contador_jugador+=1
        print(f"Jugador: {eleccion_usuario}, CPU: {eleccion_cpu}. El resultado es: {resultado}")
        print(f"Victorias del jugador:{contador_jugador}. Victorias del CPU: {contador_cpu}. Empates:{contador_empate}")
    elif resultado == "CPU":
        contador_cpu += 1
        print(f"Jugador: {eleccion_usuario}, CPU: {eleccion_cpu}. El resultado es: {resultado}")
        print(f"Victorias del jugador:{contador_jugador}. Victorias del CPU: {contador_cpu}. Empates:{contador_empate}")
    elif resultado == "EMPATE":
        contador_empate+= 1
        print(f"Jugador: {eleccion_usuario}, CPU: {eleccion_cpu}. El resultado es: {resultado}")
        print(f"Victorias del jugador:{contador_jugador}. Victorias del CPU: {contador_cpu}. Empates:{contador_empate}")
    