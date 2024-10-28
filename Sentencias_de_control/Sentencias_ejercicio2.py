'''
Nombre: Addi Toro Chávez
Fecha: 23 de Octubre de 2024
Descripción:
Ejercicio 2 de sentencias en python.

Este programa determinará la estación del año de acuerdo al número de mes ingresado por el usuario. Para ello:

a) Solicite al usuario un número que representa al mes.
b) Utilice la lógica adecuada para determinar la estación del año de acuerdo con:

    3, 4 y 5: Primavera.
    6, 7 y 8: Verano.
    9,10 y 11: Otoño.
    12, 1 y 2: Invierno.
 Otro caso: Mensaje de mes incorrecto.

c) Muestre la estación correspondiente en consola.
'''
# Ingresamos un numero de tipo entero.
numero=int(input("Ingrese numero que representa el mes del que desea saber su estacion: "))

# Establecemos las condiciones con las asignacion de rangos a la que pertenece cada estacion.
if numero >= 3 and numero <= 5:
    print("La estacion es: Primavera.")
elif numero >= 6 and numero <= 8:
    print("La estacion es: Verano.")
elif numero >= 9 and numero <= 11:
    print("La estacion es: Otoño.")
elif numero == 12 or numero == 1 or numero == 2:
    print("La estacion es: Invierno")
else:
    print("El mes no existe")