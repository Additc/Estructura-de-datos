'''
Addi Toro Chavez
9 de octubre de 2024.
Descripción:
Usos de los diferentes tipos básico de datos en Python.
'''

# Toda variable requiere un valor inicial
semestre = 3        # Se declara una variable de tipo int y le asigna el valor numerico 3.
print(semestre)     # Imprime el valor de la variable previamente definida.
semestre = 4        # La variable ya no apunta al objeto anterior, sino a uno nuevo, por lo que se pierde la referencia.
print(semestre)     # En esta parte de código la variable imprime el nuevo valor asignado.

# Se crean varias variables para ejemplificar su uso
nombre = "Addi"     # Variable de tipo String o tipo cadena.
altura = 1.71       # Variable de tipo Float o variable flotante.
edad = 19           # Variable de tipo Int o de tipo entero.

print() #El print por si solo genera un salto de linea normal.

# Se muestran en pantalla las variables en uso
print("Nombre: ",nombre)        # Imprime la cadena asignada a la variable nombre.
print("Altura: ",altura,"cm.")  # Muestra en pantalla el valor asignado a la variable de tipo flotante.
print("Edad: ",edad,"años.")    # Muestra en pantalla el valor asignado a la variable de tipo entero.
print("Semestre:",semestre)

# Se modifican los valores de las variables y se mandan a imprimir
altura = 1.75 # Se realiza la modificación del valor de la variable de tipo flotante.
edad = 20     #Se realiza la modificación del valor de la variable tipo entera
print()     # Colocación de un salto de línea.

#Se muestran en pantalla los datos con las variables ya modificadas.
print("Valores modificados:")
print("Nombre:", nombre)
print("Semestre:", semestre)
print("Altura: ", altura, "cm.")
print("Edad: ", edad, "años.")

# En Python, las variables son dinámicas, por lo que pueden almacenar otro tipo de dato en cualquier momento
edad = "treinta y uno"      # edad antes tenía el valor de 31 (Int)
print()
print("Edad (con otro tipo de dato):", edad)

# Reglas para los nombres de las variables en Python:
# - Utilizar únicamente letras (mayúsculas o minúsculas), números y el guión bajo
# - La variable no puede iniciar con números
# - No se pueden utilizar palabras reservadas, ejemplos: if, else, True, class
# - Es sensible a mayúsculas y minúsculas. Por ejemplo, las palabras "Hola", "hola" y "HOLA"

# Buenas prácticas
# - Utilizar minúsculas para las palabras
# - Separar las palabras con el guión bajo
# - Utilizar nombres descriptivos de acuerdo a su uso. Por ejemplo: edad, en lugar de e..

# Ejemplos correctos y con buenas prácticas
#Declaración de nuevas variables
fecha_nacimiento = "11 de abril del 2005"
clase = "Estructuras de Datos"
horas_estudio = 8
nombre = "Addi"
es_estudiante = True

# Ejemplos incorrectos (líneas comentadas porque marcan error) o de malas prácticas
f = "11 de abril del 2005"
fechanacimiento = "11 de abril del 2005"
# class = "Estructuras de Datos"
# 8horas_estudio = 8
Nombre = "A d d i "
NOMBRE = "Addi"

# Notar que las variables 'nombre', 'Nombre' y 'NOMBRE', son distintas
print()
print("Las variables son sensibles a mayúsculas y minúsculas:")
print("Variable nombre:", nombre)
print("Variable Nombre:", Nombre)
print("Variable NOMBRE:", NOMBRE)
