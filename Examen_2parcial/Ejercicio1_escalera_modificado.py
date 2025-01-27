"""
Nombre: Addi Toro Chavez
Fecha: 7 de diciembre del 2024
Descripción:
Ejercicio 1  exámen, escalera
"""

#Pedimos que el usuario ingre el número de escalones de la escalera
n=int(input("Ingrese el número de peldanios para la escalera: "))
# Igualo una variable que almacene el número ingresado para poder manipularlo en el siguiente caso
l=n


if n < 0:
    altura=(n*-1)
    for i in range(altura + 1):
        espacios = " " * (altura - i) * 2
        escalones = "_" if i == 0 \
            else "_|"
        print(f"{espacios}{escalones}")

if n>0:
    for i in range(l+1):
        escalones="_" if i ==0 \
        else "|_"
        espacios = " " *(i*2-1)
        print(f"{espacios}{escalones}")