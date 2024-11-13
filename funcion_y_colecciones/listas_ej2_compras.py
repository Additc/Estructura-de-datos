"""
Nombre: Addi Toro Chavez
Fecha: 12 de noviembre del 2024
Descripción:
Listas ejercicio 2
"""

nombres=[ ]
cantidades= [ ]

#Función de menú
def menu( ):
    print("Ingrese una opción:")
    print("1: Ver lista") # nombre y cantidad
    print("2: Añadir producto a la lista")
    print("3: Eliminar producto de la lista")
    print("0: Salir")
    opcion=int(input("Ingrese la opción: "))
    return opcion
opcion=menu()


def ver_lista(nombres,cantidades):
    for a in range (nombres):
        print(nombres, end = " ")
    for i in range (cantidades):
        print(cantidades, end = " ")

def añadir (compras):
    nombre=input("Ingrese nombre del producto: ")
    nombres.append=(nombre)
    cantidad=int(input("Ingrese la cantidad del producto: "))
    cantidades.appentd=(cantidad)
    return cantidades,nombres

def eliminar (nombres,cantidades):
    pos = int(input("Ingrese la pocisión del producto que desea eliminar: "))
    nombres.pop(pos)
    cantidades.pop(pos)
    return cantidades,nombres

while opcion !=0:
    opcion=menu()
    if opcion==1:
        ver_lista(nombres, cantidades)
    elif opcion==2:
        añadir(nombres,cantidades)
    elif opcion ==3:
        eliminar(nombres, cantidades)
    if opcion == 0:
        opcion=0
        print("Salió del programa")
    else:
        print("opción incorrecta")



