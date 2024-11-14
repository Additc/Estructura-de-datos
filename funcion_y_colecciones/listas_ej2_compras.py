"""
Nombre: Addi Toro Chavez
Fecha: 12 de noviembre del 2024
Descripción:
Listas ejercicio 2
"""


nombres=[ ]
cantidades= [ ]
contador_producto=0
#Función de menú
def menu( ):
    print()
    print("Seleccione una opción")
    print("1: Ver lista") # nombre y cantidad
    print("2: Añadir producto a la lista")
    print("3: Eliminar producto de la lista")
    print("0: Salir")
    opcion=int(input("Ingrese la opción: "))
    return opcion


def ver_lista(nombres,cantidades, contador_producto):
    contador_producto=1
    for nombre in nombres:
        print(f"{contador_producto}._{nombre}", end = " ")
        contador_producto+=1
    print()
    contador_producto=1
    for cantidad in cantidades:
        print(f"{contador_producto}._{cantidad} productos", end = " ")
        contador_producto+=1
    print()

def anadir ( nombres, cantidades):
    nombre=input("Ingrese nombre del producto: ")
    nombres.append(nombre)
    cantidad=int(input("Ingrese la cantidad del producto: "))
    cantidades.append(cantidad)

def eliminar (nombres,cantidades,contador_producto):
    pos = int(input("Ingrese la pocisión del producto que desea eliminar: "))
    nombres.pop(pos-1)
    cantidades.pop(pos-1)
    contador_producto-=1
    print("Producto eliminado")

op=1
while op !=0:
    opcion=menu()
    if opcion==1:
        ver_lista(nombres, cantidades, contador_producto)
    elif opcion==2:
        anadir(nombres,cantidades)
        contador_producto+=1
    elif opcion ==3:
        eliminar(nombres, cantidades,contador_producto)
    elif opcion == 0:
        op=0
        print("Salió del programa")
else:
    print("opción incorrecta")



