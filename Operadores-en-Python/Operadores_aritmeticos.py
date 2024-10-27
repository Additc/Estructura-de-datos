'''
Addi Toro Chavez
15 de octubre de 2024.
Descripción:
Clase de operadores aritméticos en python.
'''
#operadores aritméticos en python.
número1=int(input("ingrese el primer número entero: ")) # Ingresamos un número de tipo entero.
número2= int(input("ingrese el segundo número entero: ")) # Ingresamos un segundo número entero.


print(f"la suma del {número1} y del {número2} es: {número1 + número2}") # Realizamos la suma del primer número entero con el segundo número
print(f"la resta del {número1} y del {número2} es: {número1 - número2}") # Realizamos la resta del primer número con el segundo número.
print(f"la multiplicación del {número1} y del {número2} es: {número1 * número2}") # Realizamos la multiplicación del primer número por el segundo número.
print(f"la división del {número1} y del {número2} es: {número1 / número2}") # Realizamos la división del primer núero entre el segundo número.}

# En la siguiente instrucción se realiza una división, aunque la función  % (módulo), regresará el residuo de la división realizada.
print(f"el modulo del {número1} y del {número2} es: {número1 % número2}")

# En la siguiente instrucción la función // (doble diagonal) realiza una división, pero en este caso es considerada división entera.
print(f"la  del {número1} y del {número2} es: {número1 // número2}")

# En está última instrucción la función ** (doble astedisco), tiene la función de elevar el primer número dado con el segundo número dado.
print(f"la elevación del {número1} y del {número2} es: {número1 ** número2}")

