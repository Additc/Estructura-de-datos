'''
Addi Toro Chavez
16 de octubre de 2024.
Descripción:
Ejercicio de operadores de asignación compuesta en python
'''
# Asignación compuesta
numero1,numero2=int(input("ingresa numero1: ")),int(input("ingresa numero2: ")) # ingresamos 2 números
numero1+=3 # numero1 = numero1 + 3
print("suma: ",numero1)
numero2-=5 # numero2 = numero2 - 5
print("resta: ",numero2)
numero1 *=2 # numero1 = numero1 * 2
print("multiplicaion: ",numero1)
numero2 /=4 # numero2 = numero2 / 4
print("division: ",numero2)

print()
numero1,numero2=int(input("ingresa numero1: ")),int(input("ingresa numero2: ")) # ingresamos 2 números
numero1 += numero2
numero1 *= numero1
numero1 -= numero2
numero1 +=3
numero1/=2
print("el resultado es: ",numero1)

