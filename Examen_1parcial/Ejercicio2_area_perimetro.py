'''
Nombre: Addi Toro Chavez
Fecha: 27 de octubre de 2024.
Descripción:
Este programa determina el área y el perímetro de un rectángulo o de un círculo.

Muestre el siguiente menú:

    1) Calcular el área de un rectángulo.
    2) Calcular el perímetro de un rectángulo.
    3) Calcular el área de un círculo.
    4) Calcular el perímetro de un círculo.
    0) Salir.
    Cualquier otro caso -> Mostrar un mensaje de "opción no válida".

Para ello:
a) Muestre el menú anterior en consola.
b) En caso de calcular un área o perímetro, solicite al usuario los valores requeridos (flotantes).
c) Utilice la lógica adecuada para calcular lo solicitado. Asuma pi = 3.1416.
d) Imprima el resultado en la consola. Nota: muestre únicamente 3 decimales en todos los casos.
e) Repita el menú hasta salir.
'''

op =1
while op != 0:
    print("Seleccione una opcion: ")
    print("0) Salir")
    print("1) Calcular el área de un rectángulo")
    print("2) Calcular el perímetro de un rectángulo")
    print("3) Calcular el área de un círculo")
    print("4) Calcular el perímetro de un círculo")
    print()
    op=int(input(" Ingrese la opción que desea realizar: "))

    if op == 1:
        print("Calculando el área de un rectángulo: ")
        largo=float(input("Ingrese el largo del rectángulo: "))
        ancho=float(input("Ingrese ancho del rectángulo: "))
        print()
        print(f"El área del rectángulo es de: {(largo * ancho):.3f}")
        print()
    if op == 2:
        print("Calculando el perímetro de un rectángulo:")
        largo=float(input("Ingrese el largo del rectángulo: "))
        ancho=float(input("Ingrese ancho del rectángulo: "))
        print()
        print(f"El perámetro del rectángulo es de: {(largo +largo + ancho + ancho):.3f}")
        print()
    if op == 3 :
        pi = 3.1416
        print("Calculando el área de un círculo:")
        radio = float(input("Ingrese el radio del círculo: "))
        print()
        print(f"El área del círculo es de:{((radio**2)*pi):.3f} ")
        print()
    if op == 4:
        pi = 3.1416
        print("Calculando el perímetro de un círculo: ")
        radio = float(input("Ingrese el radio del círculo: "))
        print()
        print(f"El área del círculo es de:{(radio * 2 * pi):.3f} ")
        print()
    elif op == 0:
        op = 0
        print("Salió del programa")
    else:
        print("opción incorrecta")
        print()

#inicializamos nuestra opción en 1 y mostramos en pantalla el menú de opciones.
#De acuerdo a la opción que el usuario seleccione establecí las condiciones necesarias.
# Posteriormente pedí que ingresara los datos correspondientes.
# Y por último lo que el ususario decidio calcular, implemento la lógica para obtener el resultado y lo muestro en pantalla.

