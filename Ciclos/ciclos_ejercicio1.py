'''
Nombre: Addi Toro Chávez
Fecha: 28 de Octubre de 2024
Descripción:
Ejercicio 1 de ciclo while en python
'''
# Programa que calcula la suma acumulativa

numero_final=int(input("ingrese numero final de la suma: "))
contador = 0
total=0
while contador< numero_final:
    contador += 1
    total += contador
print()
print(f"La suma de 0 hasta {numero_final} es: {total}")