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