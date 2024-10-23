'''
Nombre: Addi Toro Chávez
Fecha: 23 de Octubre de 2024
Descripción:
Sentencia de condición if else if else en python
'''

#Programa que determine elgrupo de edad al que pertenece
edad=int(input("Ingrese la edad que tiene: "))
if edad <= 14 :
    print("niños y adolecentes")
elif edad>=15 and edad<=25:
    print("jovenes")
elif edad>=26 and edad<=45:
    print("adultos jovenes")
elif edad>=46 and edad<60:
    print("adultos maduros")
elif edad>=60:
    print("adultos mayores")