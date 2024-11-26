"""
Nombre: Addi Toro Chavez
Fecha: 12 de noviembre del 2024
Descripción:
Funciones ejercicio 1 calculadora básica
"""
def menu():
    print()
    print("Calculadora básica")
    print("0 Salir")
    print("1 Suma")
    print("2 Resta")
    print("3 Multiplicación")
    print("4 División")
    print("5 División entera")
    print("6 Exponenciación")
    opcion = int(input("Ingrese un número de opción a realizar: "))
    return opcion

def suma():
    print()
    numero_1 = float(input("Ingrese el primer número: "))
    numero_2 = float(input("Ingrese el segundo número: "))
    print(f"La suma del número {numero_1} y el número {numero_2} es: {numero_1 + numero_2} ")

def resta():
    numero_1 = float(input("Ingrese el primer número: "))
    numero_2 = float(input("Ingrese el segundo número: "))
    print(f"La resta del número {numero_1} y el número {numero_2} es: {numero_1 - numero_2} ")

def multiplicacion():
    numero_1 = float(input("Ingrese el primer número: "))
    numero_2 = float(input("Ingrese el segundo número: "))
    print(f"La multiplicación del número {numero_1} y el número {numero_2} es: {numero_1 * numero_2} ")

def division():
    numero_1 = float(input("Ingrese el primer número: "))
    numero_2 = float(input("Ingrese el segundo número: "))
    print(f"La división del número {numero_1} y el número {numero_2} es: {numero_1 / numero_2} ")

def division_entera():
    numero_1 = float(input("Ingrese el primer número: "))
    numero_2 = float(input("Ingrese el segundo número: "))
    print(f"La división entera del número {numero_1} y el número {numero_2} es: {numero_1 // numero_2} ")

def exponenciacion ():
    numero_1 = float(input("Ingrese el primer número: "))
    numero_2 = float(input("Ingrese el segundo número: "))
    print(f"La exponenciación del número {numero_1} y el número {numero_2} es: {numero_1 ** numero_2} ")

op=1
while op !=0:
    opcion=menu()
    if opcion == 1:
         suma()
    elif opcion == 2:
        resta()
    elif opcion == 3:
        multiplicacion()
    elif opcion == 4:
        division()
    elif opcion == 5:
        division_entera()
    elif opcion == 6:
        exponenciacion()
    elif opcion == 0:
         op=0
         print("Salió de la calculadora")
    else:
        print("Acción incorrecta")

"""
Se declaran las distintas funciones de las distintas operaciones a realizar, y a su vez una función del menú de opciones.
Con un ciclo while establezco mis condiciones de acuerdo a las opciones seleccionadas, y en cada condición llamo a la función,
que corresponde al caso.
Posteriormente se le solicitan 2 números flotantes al usuario y se muestra el resultado de la operación.
"""