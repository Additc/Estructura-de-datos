"""
Nombre: Addi Toro Chavez
Fecha: 7 de diciembre del 2024
Descripción:
Ejercicio 1  exámen, escalera
"""


n=int(input("Ingrese el número de peldanios para la escalera: "))
l=n
if n>0:
    for i in range(n+1):
        espacios=" "*(n-i)*2
        escalones="_" if i == 0 \
        else "_|"
        print(f"{espacios}{escalones}")
if n<0:
    for i in range(abs(l)+1):
        escalones="_" if i ==0 \
        else "|_"
        espacios = " " *(i*2-1)
        print(f"{espacios}{escalones}")