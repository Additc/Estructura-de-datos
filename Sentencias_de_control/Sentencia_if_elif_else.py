'''
Nombre: Addi Toro Chávez
Fecha: 23 de Octubre de 2024
Descripción:
Sentencia de condición if else if else en python
'''

#Programa que determina el grupo de edad al que pertenece

edad=int(input("Ingrese la edad que tiene: "))# Se ingresa la edad.
if edad <= 14 :# Se establece la primer condición de una determinada edad.
    print("niños y adolecentes")# Si esta primera condición se cumple se muestra en pantalla.

 # En caso contrario si no se cumple la condición anterior
# Se establecen varias condiciones, hasta que la edad entre en una de ellas , para posteriormente mostrarlo en pantalla
elif edad>=15 and edad<=25: # Se establece otra condición con otro rango de edad.
    print("jovenes")
elif edad>=26 and edad<=45:# Se establece otra condición con otro rango de edad.
    print("adultos jovenes")
elif edad>=46 and edad<60:# Se establece otra condición con otro rango de edad.
    print("adultos maduros")
elif edad>=60:# Se establece otra condición con otro rango de edad.
    print("adultos mayores")