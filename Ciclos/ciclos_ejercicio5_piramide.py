"""
Nombre: Addi Toro Chavez
Fecha: 6 de noviembre del 2024
Descripción:
ciclo for, ejercicio 5 pirámide
"""

n = int(input("ingrese múmero de filas: "))
k=n
l=n
for i in range(1,n+1):
    astediscos="*"*i
    print(f"{astediscos}")
print()

for i in range(1,k+1):
    astediscos="*"*k
    print(f"{astediscos}",end=" ")
    k-=1
    print()

print()
for i in range(0,l+1):
    astediscos="*"*l
    espacio = " " * i
    print(f"{espacio}{astediscos}",end=" ")
    l -= 1
    print()

for i in range(1,n+1):
    astediscos="*"* i
    espacio= " "* n
    print()
    print(f"{espacio}{astediscos}", end = " ")
print()
