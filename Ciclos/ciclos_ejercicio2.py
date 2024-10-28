'''
Nombre: Addi Toro Chávez.
Fecha: 28 de Octubre de 2024
Descripción:
Ejercicio 1 de ciclo while en python
'''
numero_inicial=int(input("ingrese numero inicial: "))
numero_final=int(input("ingrese numero final de la suma: "))
total=0
while numero_inicial< numero_final:
    numero_inicial += 1
    total += numero_inicial
print()
print(f"La suma de {numero_inicial} hasta {numero_final} es: {total}")