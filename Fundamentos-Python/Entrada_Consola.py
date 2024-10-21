'''
Nombre: Addi Toro Chávez
Fecha: 19 de Octubre de 2024
Descripción:
Entrada de datos por consola para interacturar con el usuario con valores dinámicos.
'''

# Comentar sobre la función input.
# La función input la utilizamos para leer una entrada de datos desde la terminal.
# Donde esperaremos que el usuario escriba algo, luego, los datos introducidos los almacenamos en una variable.
# Pedimos dos números al usuario por consola y las almacenamos en diferentes variables.
numero1_cadena = input("Introduce un número decimal: ") # Los datos introducidos por el usuario regresan como una cadena.
numero2_cadena = input("Introduce otro número decimal: ")
"""
En la proxima instrucción se intentar hacer la suma de los 2 datos introducidos sin embargo esta acción no se puede realizar 
ya que estan guardadas como cadenas.
"""
resultado_cadena = numero1_cadena + numero2_cadena
print()
print(" ****  Recibir número sin un casting de varibles  ****")
# Muestra en pantalla la comcatenación de ambas cadenas.
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}")

nose_float = float(input("Ingresa un número: "))

# Comentar por qué se realiza el casting de variables.
numero1_float = float(numero1_cadena)#El número ingresado por el usuario lo convertimos a un valor flotante y lo en una variable.
numero2_float = float(numero2_cadena)#El número ingresado por el usuario lo convertimos a un valor flotante y lo en una variable.

resultado_float = numero1_float + numero2_float # Verificar qué es lo que realiza de esta manera y compáralo.
# Realizamos la suma de los 2 números flotantes y en este caso se puede realizar correctamente por que ahora ambos  son decimales y no cadenas.
print()
print(" ****  Casting de varibles  ****")
# Al imprimir, se imprimirá la suma de los números y no los concatenará.
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")
