'''
Nombre: Addi Toro Chávez
Fecha: 23 de Octubre de 2024
Descripción:
Ejercicio 1 de sentencia en python.

Este programa determinará cuál de dos números ingresados por el usuario es menor o si son iguales. Para ello:

a) Solicite al usuario dos números decimales.
b) Utilice la lógica adecuada para determinar cuál de los dos números es menor o si es que son iguales.
c) Muestre el número menor (o que son iguales) en consola.
'''

#Ingresamos 2 número de valor flotante.
numero_1=float(input("ingrese el primer número: "))
numero_2=float(input("ingrese el segundo número: "))

# Establecemos las condiciones con las sentencias if, elif y else
if numero_1 > numero_2:
    print(f"El número {numero_2} es menor que el número {numero_1} ")
elif numero_1 < numero_2:
    print(f"El número {numero_1} es menor que el número {numero_2} ")
else:
    print(f"Los números {numero_1} y el número {numero_2} son iguales. ")

