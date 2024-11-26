"""
Nombre: Addi Toro Chavez
Fecha: 6 de noviembre del 2024
Descripción:
ciclo for, ejercicio 5 pirámide
"""

n = int(input("ingrese múmero de filas: "))
k=n
l=n
h=n
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


for k in range(0, h):
    asteriscos = "*" * (2 * k + 1)
    espacios = " " * (h - k - 1)
    print(f"{espacios}{asteriscos}")
print()

"""
Pido al usuario que ingrese el número de filas que desea ver en la pirámide.
Para evitar confusiones con el mismo contador, igualo distintas variables al número de filas.
Declaro los distintas condiciones (for) y dependiendo de la forma de la pirámide implemento la lógica necesaria.
Por último se muestra en pantalla las pirámides.
"""