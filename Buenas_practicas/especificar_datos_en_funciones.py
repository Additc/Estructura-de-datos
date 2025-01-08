'''
Nombre: Addi Toro Chavez
Fecha: 8 de enero de 2025.
Descripción: Especifícar datos en funciones.
'''
def cadena_a_entero (cadena:str)->int|None:
    no_guiones=cadena.count("-")
    revisar_cadena=cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0,1):
        return int(cadena)
    else:
        return None

opcion =0
if opcion==2:
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
