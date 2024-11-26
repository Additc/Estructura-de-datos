"""
Nombre: Addi Toro Chavez
Fecha: 16 de noviembre del 2024
Descripción:
Tuplas ejercicio máximo y mínimo
"""
numeros=[]
#Función de menú
def menu( ):
    print()
    print("Seleccione una opción")
    print("1: Ver lista de números") # nombre y cantidad
    print("2: Añadir numero a la lista")
    print("3: Determinar el número mayor y menor de la lista")
    print("0: Salir")
    opcion=int(input("Ingrese la opción: "))
    return opcion


def ver_lista(numeros):
    if len(numeros)==0:
        print("No hay números")
    else:
        print(numeros)
    print()

def anadir (numeros):
    numero=input("Ingrese número a la lista: ")
    numeros.append(numero)
    print("Agregado correctamente")

def mayor_menor(numeros):
        if len(numeros) == 0:
            return ()

        mayor = numeros[0]
        menor = numeros[0]
        for numero in numeros:
            if numero > mayor:
                mayor = numero
            if numero < menor:
                menor = numero
        print()
        return (mayor, menor)

def mostrar_numeros(numeros):
    resultado = mayor_menor(numeros)
    if len(resultado) == 0:
        print("No hay números")
    else:
        print(f"El número máximo de la lista es: {resultado[0]}")
        print(f"El número mínimo de la lista es: {resultado[1]}")
        print()

op=1
while op !=0:
    opcion=menu()
    if opcion==1:
        ver_lista(numeros)
    elif opcion==2:
        anadir(numeros)
    elif opcion ==3:
        mostrar_numeros(numeros)
    elif opcion == 0:
        op=0
        print("Salió del programa")
else:
    print("opción incorrecta")

"""
Declaro una lista, que almacenara los numero proporcionados por el usuario.

Posteriormente defino mis funciones, de menú, para ver lista,obterner el mayor y menor y mostrarlo, a cada una de las funciones
les mando la lista previamente declarada, e implemento la lógica para que cada función cumpla con su deber.

Con una condición while, establezco mis condiciones de opciones del menú y hago la llamada de las funciones correspondientes,
según sea el caso.
"""