"""
Nombre: Addi Toro Chavez
Fecha: 12 de noviembre del 2024
Descripción:
Funciones ejercicio 2 piámide
"""

def forma1(n):
    print("Forma 1:")
    for i in range(1,n+1):
        astediscos="*"*i
        print(f"{astediscos}")
    print()

def forma2(n):
    k=n
    print("Forma 2:")
    for i in range(1,k+1):
        astediscos="*"*k
        print(f"{astediscos}",end=" ")
        k-=1
        print()
    print()
def forma3(n):
    l=n
    print("Forma 3:")
    for i in range(0,l+1):
        astediscos="*"*l
        espacio = " " * i
        print(f"{espacio}{astediscos}",end=" ")
        l -= 1
        print()

def forma4(n):
    h=n
    print("Forma 4:")
    for k in range(0, h):
        asteriscos = "*" * (2 * k + 1)
        espacios = " " * (h - k - 1)
        print(f"{espacios}{asteriscos}")
        print()

n = int(input("ingrese múmero de filas: "))
forma1(n)
forma2(n)
forma3(n)
forma4(n)

"""
Declaro mis distintas funciones para las 4 formas de las pirámides, dependiendo de la forma de la pirámide implemento
la logicá dentro de ellas con ayuda del ciclo (for) y mandando a cada una de ella el número de filas que el usuario desea.

Pido al usuario que ingrese el número de filas que desea ver en la pirámide.

Por último se muestra en pantalla las 4 formas de las pirámides.
"""