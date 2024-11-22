'''
Nombre: Addi Toro Chávez.
Fecha: 28 de Octubre de 2024
Descripción:
Ejercicio suma acumulativa 2 de ciclo while en python
'''
numero_inicial=int(input("ingrese numero inicial: "))
numero_final=int(input("ingrese numero final de la suma: "))
total=0
while numero_inicial< numero_final:
    numero_inicial += 1
    total += numero_inicial
print()
print(f"La suma de {numero_inicial} hasta {numero_final} es: {total}")
"""
Pedimos al usuario que ingrese el número inicial y el número final hasta el cual llegara la suma accumulativa.
Declaró un contador y una variable que almacenará la suma acumulativa, y los inicializo en cero.
Establezco la condición while que detendrá la suma acumulativa, hasta que el contador sea menor al número final ingresado.
Posteriormente elcontador incrementara uno en uno, para posteriormente guardar la suma de los numeros en otra variable.
Por último mostrará en pantalla el número inicial ingresado, el número final y el resultado de la suma acumulativa. 
"""