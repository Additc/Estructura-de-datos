'''
Addi Toro Chavez
27 de octubre de 2024.
Descripción:
Ejercicio 4 de ciclo while en python
 calculadora basica
'''


op=1
while op !=0:
    print()
    print("Calculadora básica")
    print("0 Salir")
    print("1 Suma")
    print("2 Resta")
    print("3 Multiplicación")
    print("4 División")
    print("5 División entera")
    print("6 Exponenciación")
    op = int(input("Ingrese un número de opción a realizar: "))

    if op == 1:
        print()
        numero_1 = float(input("Ingrese el primer número: "))
        numero_2 = float(input("Ingrese el segundo número: "))
        print(f"La suma del número {numero_1} y el número {numero_2} es: {numero_1 + numero_2} ")
    elif op == 2:
        numero_1 = float(input("Ingrese el primer número: "))
        numero_2 = float(input("Ingrese el segundo número: "))
        print(f"La resta del número {numero_1} y el número {numero_2} es: {numero_1 - numero_2} ")
    elif op == 3:
        numero_1 = float(input("Ingrese el primer número: "))
        numero_2 = float(input("Ingrese el segundo número: "))
        print(f"La multiplicación del número {numero_1} y el número {numero_2} es: {numero_1 * numero_2} ")
    elif op == 4:
        numero_1 = float(input("Ingrese el primer número: "))
        numero_2 = float(input("Ingrese el segundo número: "))
        print(f"La división del número {numero_1} y el número {numero_2} es: {numero_1 / numero_2} ")
    elif op == 5:
        numero_1 = float(input("Ingrese el primer número: "))
        numero_2 = float(input("Ingrese el segundo número: "))
        print(f"La división entera del número {numero_1} y el número {numero_2} es: {numero_1 // numero_2} ")
    elif op == 6:
        numero_1 = float(input("Ingrese el primer número: "))
        numero_2 = float(input("Ingrese el segundo número: "))
        print(f"La exponenciación del número {numero_1} y el número {numero_2} es: {numero_1 ** numero_2} ")
    elif op == 0:
         op=0
         print("Salio de la calculadora")
    else:
        print("Acción incorrecta")

"""

"""