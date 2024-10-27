'''
Addi Toro Chavez
27 de octubre de 2024.
Descripción:
Ejercicio número 4 de operadores en  python

Este programa determinará True o False de acuerdo a la expresión (exp1 O exp2) Y (exp3 O exp4). Para ello:

a) Pida al usuario cuatro valores booleanos (V/F).
b) Obtenga el resultado de la expresión booleana de acuerdo con los valores ingresados.
c) Muestre el resultado en consola como valor booleano (True/False).
'''

#Pedimos al usuario que ingrese los valores booleanos (verdadero,falso)
exp1=input("Ingrese el valor booleano (V,F): ")
exp2=input("Ingrese el valor booleano (V,F): ")
exp3=input("Ingrese el valor booleano (V,F): ")
exp4=input("Ingrese el valor booleano (V,F): ")

exp1= exp1.lower()=="v"
exp2= exp2.lower()=="v"
exp3= exp3.lower()=="v"
exp4= exp4.lower()=="v"

# Se muestra en pantalla el resultado de la operación booleana.
print(f"El resultado de la expresion booleana es: {(exp1 or exp2) and (exp3 or exp4)}")