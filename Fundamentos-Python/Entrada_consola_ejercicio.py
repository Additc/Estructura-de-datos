'''
Nombre: Addi Toro Chávez
Fecha: 19 de Octubre de 2024
Descripción:
Ejercicio con respecto a datos por consola en python

Escribe un programa de nombre Entrada_consola_ejercicio.py que realice lo siguiente:

a) Pida 2 números decimales por consola al usuario utilizando la función input.

b) Muestre los resultados de las operaciones básicas con esos números: suma, resta, multiplicación y división.

Nota: Asuma que el usuario siempre va a ingresar números y que el segundo número es diferente de cero.

'''
#Ingresamos los números decimales por consola y los guardamos en una variable.
float_1=float(input("ingrese primer numero decimal: "))# Ingresamos primer número decimal.
float_2=float(input("ingrese primer numero decimal: "))# Ingresamos segundo número decimal.

print(f"El primer número {float_1} más la suma el segundo número {float_2} es: {float_1 + float_2}")# Se realiza la suma de los 2 números decimales.
print(f"El primer número {float_1} menos  el segundo número {float_2} es: {float_1 - float_2}")# Se realiza la resta del primer número decimal menos el segundo número decimal.
print(f"El primer número {float_1} multiplicado por el segundo número {float_2} es: {float_1 * float_2}")# Se realiza la multiplicación del primer número decimal por el segundo.
print(f"El primer número {float_1} dividido por el segundo número {float_2} es:  {(float_1 / float_2):.2f}")# Se realiza la division del primer número decimal entre el segundo.