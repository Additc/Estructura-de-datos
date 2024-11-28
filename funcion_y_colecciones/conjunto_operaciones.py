'''
Addi Toro Chavez
27 de octubre de 2024.
Descripción:
Ejercicio 26 de ciclo while en python
 calculadora básica
'''
from random import randint
#numeros aleatorios en una lista
randint(1,4)->numero
ganador=random.choice(lista)


conjunto_A={11,7,10,9,5,1,15,7}
conjunto_B={55,70,11,77,66,9,5}
print(conjunto_A)
print(conjunto_B)
print()
#Operaciones básicas
#unión
union=conjunto_A|conjunto_B
print(union)
print()

#intersección(aparecen en los 2 conjuntos)
inteseccion=conjunto_A & conjunto_B
print(inteseccion)

#Diferencia entre conjuntos A y B
diferencia= conjunto_A & conjunto_B
print(diferencia)
print()

#Una lista
print("lista de animales")
animales=["leon","leopardo","tigre","jaguar","aguila"]
print(animales)
print()
#convertir de listas a conjuntos viceversa
conjunto=set(animales)
print(conjunto)
print()

lista_modificada=list(conjunto)# De una lista a un conjunto
print(lista_modificada)

lista_modifocada2=tuple(conjunto)#De tuplas a conjuntos

