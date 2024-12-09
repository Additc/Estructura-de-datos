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

#Si el número ingresado es positivo, inicia el ciclo for y ejecuta la lógica mostrada
if n>0:
    for i in range(n+1):
        espacios=" "*(n-i)*2
        escalones="_" if i == 0 \
        else "_|"
        print(f"{espacios}{escalones}")
#En caso contrario que sea un número negativo, realiza el siguiente proceso.
if n<0:
    for i in range(abs(l)+1):
        escalones="_" if i ==0 \
        else "|_"
        espacios = " " *(i*2-1)
        print(f"{espacios}{escalones}")