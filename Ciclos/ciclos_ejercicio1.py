'''
Nombre: Addi Toro Chávez
Fecha: 28 de Octubre de 2024
Descripción:
Ejercicio suma acumulativa 1 de ciclo while en python
'''
# Programa que calcula la suma acumulativa de números

numero_final=int(input("ingrese número final de la suma: "))
contador = 0
total=0
while contador< numero_final:
    contador += 1
    total += contador
print()
print(f"La suma de 0 hasta {numero_final} es: {total}")
"""
Pedimos al usuario que ingrese el número final hasta el cual llegara la suma accumulativa.
Declaró un contador y una variable que almacenará la suma acumulativa, y los inicializo en cero.
Establezco la condición while que detendrá la suma acumulativa, hasta que el contador sea menor al número final ingresado.
Posteriormente elcontador incrementara uno en uno, para posteriormente guardar la suma de los numeros en otra variable.
Por último mostrará en pantalla el número inicial ingresado y el resultado de la suma acumulativa. 
"""