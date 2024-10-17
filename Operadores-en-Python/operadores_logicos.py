'''
Addi Toro Chavez
16 de octubre de 2024.
Descripción:
Ejercicio de operadores lógicos en python
'''
expresion1, expresion2=input("¿te  gusta el futbol? si/no: ") , input("te gusta el basquetbol si/no: ")
expresion1 = expresion1.lower() == "si" # condicion para devolver true o false
expresion2 = expresion2.lower() == "si"
print(expresion1)
print(expresion2)

print(f"¿Ambas respuestas son verdaderas? {expresion1 and expresion2}")
print(f"¿Una respuesta fue verdadera? {expresion1 or expresion2}")
print(f"La negación de la primera respuesta es: { not expresion1}")
print(f"La negación de la segunda respuesta es: { not expresion2}")