'''
Addi Toro Chavez
9 de octubre de 2024.
Descripción:
ejercicio formativo de tipo de datos
'''
""""
Addi Toro Chavez
10 de octubre de 2024.
Descripción:
Ejercicio de casting perteneciente a la tercera clase, de introducción al lenguaje de programación python

Descripción del ejercicio:

Realiza un programa de nombre Casting_ejercicio.py que realice lo siguiente:

a) Convierta los siguientes números en cadenas: 3.14159265, 12, 0.

b) De los números anteriores, indica su valor booleano.

c) Convierta las siguientes cadenas a números: "10002", "100.02", "0".

d) De las cadenas anteriores, indica su valor booleano. Nota: especificar por qué el resultado de la cadena "0".

"""

#  a) Conversión de los siguientes números en cadenas:

# Creamos las variables y asignamos un valor, para posoteriormente tranformarlo al tipo de dato cadena
var_int1 = 12
var_int = 0
var_float = 3.14159265
print()
print("Conversión de número a cadena.")
print(f"Los números {var_int},{var_int1} y {var_float} se convierten a cadena utilizando str(var_int): {str(var_int)},{str(var_int1)} y "
      f"str(var_float): {str(var_float)}.")

print()

# b) Indicando  el booleano de  los valores anteriores:
# Verificación de booleano en los valores (true,false) 

es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")


es_verdadero = bool(var_int1)
print(f"¿El valor de {var_int1} es verdadero? {es_verdadero}.")


es_verdadero = bool(var_float)
print(f"¿El valor de {var_float} es verdadero? {es_verdadero}.")

print()
# c) Conversión de las siguientes cadenas a números:

var_cadena = "10002"
var_int = int(var_cadena)
print("el valor de la cadena a entero es: ",var_int)

var_cadena1 = "0"
var_int1 = int(var_cadena1)
print("el valor de la cadena a entero es: ",var_int1)

var_cadena2 = "100.02"
var_float = float(var_cadena)
print("el valor de la cadena a entero es: ",var_float)

print()
# d) Indicación del valor boleano de las cadenas anteriores

es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")

es_verdadero = bool(var_cadena1)
print(f"¿El valor de {var_int1} es verdadero? {es_verdadero}.")

es_verdadero = bool(var_cadena2)
print(f"¿El valor de {var_cadena2} es verdadero? {es_verdadero}.")

# Es considerado verdadero por que en este caso el tipo de dato es cadena y en caso contrario, si el tipo de dato fuera entero fuera falso 
print("addi")
