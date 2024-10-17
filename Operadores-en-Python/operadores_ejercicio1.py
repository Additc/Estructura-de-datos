'''
Addi Toro Chavez
17 de octubre de 2024.
Descripción:
Ejercicio de operadores relacionales en python
'''

compra=float(input("ingrese la cantidad de compra: "))
expresion1=input("¿compras a meses sin intereses? si/no: ")
expresion1 = expresion1.lower() == "si" # condicion para devolver true o false
print(f"¿Aplica bonificación?{ compra >= 5000 and expresion1}")
print()
