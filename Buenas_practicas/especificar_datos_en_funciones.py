'''
Nombre: Addi Toro Chavez
Fecha: 8 de enero de 2025.
Descripción: Especifícar datos en funciones.
terminar hoy
'''

def menu ():
    print("conversión de números")
    print("1) De cadena a flotante")
    print("2) De cadena a entero")
    print("0) Salir")
    opcion=(input("Teclea la opción que desea realizar: "))
    while not opcion.isnumeric():
        print("opción no válida")
        opcion= input("ingrese número nuevamente: ")
    opcion=int(opcion)
    return opcion


def cadena_a_flotante (cadena):
    no_puntos=cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".","")
    if revisar_cadena.isnumeric() and no_puntos in (0,1) and no_guiones in (0,1):
        return float(cadena)
    else:
        return None

def cadena_a_entero (cadena:str)->int|None:
    no_guiones=cadena.count("-")
    revisar_cadena=cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0,1):
        return int(cadena)
    else:
        return None

op=1
while op!=0:
    opcion = menu()
    if opcion==1:
        num_cadena=input("ingrese número a convertir: ")
        numero=cadena_a_flotante(num_cadena)
        while numero is None:
            num_cadena = input("opcion invalida, intente nuevamente: ")
            numero = cadena_a_entero(num_cadena)
        print(f"El número {numero} es de tipo {type(numero)}")
    elif opcion==2:
        num_cadena= input("ingrese número a convertir: ")
        numero=cadena_a_entero(num_cadena)
        while numero is None:
            num_cadena = input("opcion invalida, intente nuevamente: ")
            numero = cadena_a_entero(num_cadena)
        print(f"El número {numero} es de tipo {type(numero)}")
    elif opcion == 0:
        opcion = 0
        print("Salió del programa")
    else:
        print("opcion incorrecta")
