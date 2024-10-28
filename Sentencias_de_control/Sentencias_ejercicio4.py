'''
Nombre: Addi Toro Chávez
Fecha: 23 de Octubre de 2024
Descripción:
Ejercicio 3 de sentencias en python.
Este programa determinará si te permiten el acceso al bar "La Negra", por lo que se debe cumplir lo siguiente:

    Tener al menos 18 años.
    Tener al menos $ 250.00 para gastar.

Si ambas condiciones se cumplen, se imprime el mensaje en consola: "¡Bienvenido a tu mejor bar!". En caso contrario, se imprime: "Lo sentimos, ya estamos por cerrar!"

Para ello:
a) Solicite al usuario su edad.
b) Solicite al usuario el dinero con el que cuenta.
c) Utilice la lógica adecuada para determinar el mensaje.
d) Muestre el mensaje adecuado en consola
'''

edad=int(input("Ingrese su edad: "))
dinero=int(input("Ingrese el dinero a gastar: "))

if edad >= 18 and dinero >= 250:
    print("¡Bienvenido a tu mejor bar!")
else:
    print("Lo sentimos, ya estamos por cerrar")