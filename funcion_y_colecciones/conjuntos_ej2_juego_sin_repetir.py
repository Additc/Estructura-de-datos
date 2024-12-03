"""
Nombre: Addi Toro Chavez
Fecha: 25 de noviembre del 2024
Descripción:
Conjuntos ejercicio 2 juego sin repetir.
"""

palabras_juego=set()
contador_palabras=1
print("Juego sin repetir")
print("reglas: ")
print("Este es un juego que se puede jugar de manera grupal, en donde el objetivo es decir palabras de un tema en específico y los jugadores deben tratar de no repetir la misma palabra.")
print()
temas = input("Ingrese tema del juego: ")


for i in range (100):
    palabra=input(f"Ingrese la palabra {contador_palabras} del tema {temas}: ")
    if (palabra in palabras_juego):
        print(f"El juego ha terminado! Han dicho {contador_palabras} palabras diferentes.")
        print(f"Las palabras fueron {palabras_juego}")
        break
    else:
        palabras_juego.add(palabra)
        contador_palabras += 1
"""
Declaro un conjunto vacío que almacenará las palabras introducidas por el usuario, y además un conador para llevar el número de palabras introducidas.
Se muestra en pantalla las reglas del juego, para posteriormente seleccionar un tema sobre el juego.
Establezco un ciclo (while) que estará repitiendo el juego hasta 100 palabras, siempre y cuando no se cumpla la condición de que alguna palabra se repita.
en dado caso se muestra en pantalla el número de palabras ingresadas y las palsbras ingresadas.
 
"""