"""
Nombre: Addi Toro Chavez
Fecha: 25 de noviembre del 2024
Descripción:
Conjuntos
"""

# Un conjunto es desoordenado y mutable
print("**Ejemplo de uso de conjuntos**")

#Crear un conjunto vacio
conjuntos_nombre= set()
print(f"Conjunto vacio: {conjuntos_nombre}")

#Se aniaden valores al conjunto
conjuntos_nombre.add("rebeca")
conjuntos_nombre.add("galilea")
conjuntos_nombre.add("juan")
conjuntos_nombre.add("marlene")
conjuntos_nombre.add("paty")
conjuntos_nombre.add("ryan")
conjuntos_nombre.add("Tania")
conjuntos_nombre.add("Addi")
conjuntos_nombre.add("Yamm")
conjuntos_nombre.add("Hector")
conjuntos_nombre.add("Alberto")
conjuntos_nombre.add("rosalinda")
print(f"Conjunto 303: {conjuntos_nombre}")
print()

#Aniadir elementos repetidos
#Esto no se puede aniadir duplicados a un conjunto
conjuntos_nombre.add("Addi")
print(f"conjunto 303: {conjuntos_nombre}")
print()

#Se eliminan elementos de un conjunto, se elimina con una cadena o valor
conjuntos_nombre.remove("juan")
print(f"conjunto 303: {conjuntos_nombre}")
print()

#Mostrar todos los elementos
for nombre in conjuntos_nombre:
    print(nombre,end=",")

print()
#Verificar si un elemento pertenece a un conjunto
name="juan"
print(f"El elemento {name} pertenece al conjunto?{name in conjuntos_nombre} ")

#Conjunto de numeros
conjuntos_numero={1.5,11.10,10.11,7.2,8.9} #Declaracion de un conjunto de numeros

#Funciones basicas:
#Tamanio del conjunto
len(conjuntos_numero)

#Suma de elementos
sum(conjuntos_numero)



#Plataforma educativa en conjuntos
"""
Un conjunto en Python es una colección desordenada de elementos únicos. Esto significa que:
- No hay elementos duplicados: Cada elemento aparece solo una vez en el conjunto.
- No hay orden: Los elementos no están ordenados de ninguna manera específica.
- Son mutables: Se puede modificar después de crearlo, agregando o eliminando elementos.

Sintaxis para crear un conjunto:
Se encierra los elementos entre llaves {} y se separan por comas. 
Nota: Lo anterior aplica, excepto para crear un conjunto vacío.

"""


# Se crea un conjunto vacío y se imprime.
print("          ********  Ejemplos de uso de conjuntos  ********")

conjunto_nombres = set()        # Se utiliza la función set() para crear un conjunto vacío.

print(f"Conjunto vacío: {conjunto_nombres}")
print()

# Se añaden elementos al conjunto.
# Como los conjuntos no son ordenados. No se garantiza que se muestran de la manera en que se añaden.
print("Se añaden valores al conjunto.")

conjunto_nombres.add("Alberto")
conjunto_nombres.add("Yare")
conjunto_nombres.add("Alejandra")
conjunto_nombres.add("Diego")
conjunto_nombres.add("Kike")
conjunto_nombres.add("Laura")
conjunto_nombres.add("Yaki")

print(f"Conjunto con elementos añadidos: {conjunto_nombres}")
print()

# Se añaden elementos repetidos.
print("Se intenta añadir elementos repetidos al conjunto.")

print(f"Conjunto antes de añadir elementos repetidos: {conjunto_nombres}")
conjunto_nombres.add("Alberto")
conjunto_nombres.add("Yare")

print(f"Conjunto después de añadir elementos repetidos: {conjunto_nombres}")
print()

# Se eliminan elementos del conjunto.
print("Se eliminan elementos del conjunto.")

print(f"Conjunto antes de eliminar elementos: {conjunto_nombres}")
conjunto_nombres.remove("Diego")

print(f"Conjunto después de eliminar elementos: {conjunto_nombres}")
print()

# Se muestran los elementos del conjunto, tal como las listas y tuplas.
print("Se muestran los elementos del conjunto utilizando el ciclo for.")

for nombre in conjunto_nombres:
    print(f"Hola {nombre}", end = ", ")
print()
print()

# Se comprueba si existe un valor en el conjunto.
print("Se comprueba si existe un valor en el conjunto.")
nombre1 = "Alberto"
nombre2 = "Diego"

print(f"¿El nombre {nombre1} lo contiene el conjunto? {nombre1 in conjunto_nombres}")
print(f"¿El nombre {nombre2} lo contiene el conjunto? {nombre2 in conjunto_nombres}")
print()

# Funciones básicas con conjuntos.
# Se utiliza otro conjunto, en este caso, de números.
print("Funciones básicas que se utilizan en los conjuntos.")

conjunto_numeros = {12.1, 1.1, 3.3, 4.5}

print(f"Conjunto de números: {conjunto_numeros}")
print(f"Tamaño del conjunto con la función len(): {len(conjunto_numeros)}")
print(f"Suma de los elementos del conjunto con la función sum(): {sum(conjunto_numeros)}")
print()