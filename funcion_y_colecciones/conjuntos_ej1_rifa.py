"""
Nombre: Addi Toro Chavez
Fecha: 25 de noviembre del 2024
Descripción:
Conjuntos ejercicio 1 rifa.
"""
correos=[ ]
contador_correos=0

def menu( ):
    print()
    print("Seleccione una opción")
    print("1: Ver correos de los participantes") # nombre y cantidad
    print("2: Agregar correo de participante")
    print("3: Eliminar correo de participante")
    print("4: Sellecionar un ganador")
    print("0: Salir")
    opcion=int(input("Ingrese la opción: "))
    return opcion

def ver_correos(correos,contador_correos):
    contador_correos=1
    for correo in correos:
        print(f"{contador_correos}._{correo}", end = " ")
        contador_correos+=1
    print()

def agregar_correo(correos,contador_correos):
    contador_correos =1
    correo=input(f"Ingrese correo del participante {contador_correos}: ")
    correos.append(correo)

def eliminar_correo(correos, contador_correos:
    pos=int(input("Ingrese pocisión del participante que desea eliminar: "))
    correos.pop(pos - 1)
    contador_correos-= 1
    print("Producto eliminado")


def selecciona_ganador(correos, contador_correos):



op = 1
while op != 0:
    opcion = menu()
    if opcion == 1:
        ver_correos(correos, contador_correos)
    elif opcion == 2:
        agregar_correo(correos, contador_correos)
        contador_correos += 1
    elif opcion == 3:
        eliminar_correo(correos, contador_correos)
    elif opcion == 4:
        selecciona_ganador(correos, contador_correos)
    elif opcion == 0:
        op = 0
        print("Salió del programa")
else:
    print("opción incorrecta")