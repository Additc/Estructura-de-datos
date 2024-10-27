'''
Addi Toro Chavez
17 de octubre de 2024.
Descripción:
Ejercicio número 2 python
'''

expresion1, expresion2=input("¿Es profesor de la UNSIJ? si/no: ") , input("Es estudiante de la UNSIJ si/no: ")
expresion1 = expresion1.lower() == "si" # condicion para devolver true o false
expresion2 = expresion2.lower() == "si"

print(f"¿Forma parte de la comunidad UNSIJ?: {expresion1 or expresion2}") #Se muestra en pantalla el resultado de la comparación.