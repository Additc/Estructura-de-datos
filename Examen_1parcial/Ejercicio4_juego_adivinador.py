'''
Nombre: Addi Toro Chavez
Fecha: 27 de octubre de 2024.
Descripción:
Este programa es un juego en donde el usuario intente adivinar un número secreto.


Para ello:
a) El número a adivinar es un número aleatorio entre 1 y 100.
b) El jugador tendrá 5 intentos para encontrar el número.
c) Como pista, el juego indicará si el número a adivinar es menor o mayor al número ingresado, si el número no es el correcto.
d) Si el jugador adivina el número, el juego muestra un mensaje de felicitación y el número de intentos.
e) Si el jugador no adivina el número, el juego muestra un mensaje con el número.
'''
# Importó la librería para los números aleatorios
from random import randint
import random
CPU = randint(1,100)# La computadora genera un número aleatorio entre uno y cien.
numero_intento = 1 #Inicializo un contador que me mostrará los números de intentos que el usuario lleva.
print("**Juego del adivinador**")
while numero_intento <= 5: # Establezco una condición que marcará el límite de intentos
    print(f" Numero de intento: {numero_intento }", end=" ")
    numero_jugador = int(input("Ingrese numero (1-100): "))# Muestro en pantalla el número de intentos y el usuario ingresa un número cualquiera.
    if CPU>numero_jugador: # Establezco las condiciones que indicarán si el numero a adivinar el mayor o menor al ingresado.
        print("El numero a adivinar es mayor")
        numero_intento +=1 # Aumento el contador de número de intentos en dado caso que no adivine el número.
    elif CPU<numero_jugador:
        print(f"El numero a adivinar es menor")
        numero_intento +=1
    else:
        print(f"Felicidades adivinaste en: {numero_intento} intentos") # Si el ususario adivina el número, se muestra en pantalla el número de intentos en el que lo logró.
        break
    if numero_intento == 6:
        print(f"Perdiste. El numero era: {CPU}") # Si no adivina el número en 5 intentos, le muestra el resultado.
        break
