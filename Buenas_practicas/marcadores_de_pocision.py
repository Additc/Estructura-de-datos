'''
Nombre: Addi Toro Chavez
Fecha: 8 de enero de 2025.
Descripción: marcadores de pocisión.
'''
#TODO implemenrtar menú
def menu ():
    pass #sirve para dejarlo como algo pendiente de hacer

#TODO implementar cadena a entero de
def cadena_a_entero(cadena):
    pass

#FIXME revisar caso n=0 (funciona para revisar detalles dentro del código)
def cadena_a_flotante (cadena):
    raise NotImplementedError("implementar función")

#TODO implementar menú
opcion=menu()
while opcion !=0:
    if opcion==1:
        num_cadena=input("ingrese número a convertir: ")
        num=cadena_a_entero(num_cadena)
    if opcion==2:
        num_cadena= input("ingrese número a convertir: ")
        num=cadena_a_flotante(num_cadena)
    elif opcion == 0:
        opcion = 0
        print("Salió del programa")
    else:
        print("opcion incorrecta")
