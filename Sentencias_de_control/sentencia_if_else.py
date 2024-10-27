'''
Nombre: Addi Toro Chávez
Fecha: 23 de Octubre de 2024
Descripción:
Sentencia de condición if else en python
'''

#else si la primera condición no es verdadera
#Programa que determina si un numero es par o impar
numero=int(input("ingrese un numero: ")) # ingresamos el número

if numero % 2==0: #Establecemos la condición,  si el módulo del número es 0 .
    print(f"el numero {numero} es par") # Mostrará en pantalla que es un número par, si la primera condición se cumple.

else: # En caso contrario que la primera condición no se cumpla.
    print("es impar") # Muestra en pantalla que es un número impar.
