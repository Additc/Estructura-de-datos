# Toda variable requiere un valor inicial
semestre = 3        # se declara una variable de tipo int y le asigna el valor numerico 3
print(semestre)     # imprime el valor de la variable
semestre = 4        # la variable ya no apunta al objeto anterior, sino a uno nuevo, por lo que se pierde la referencia
print(semestre)

# Se crean varias variables para ejemplificar su uso
nombre = "Addi"     # variable de tipo String
altura = 1.71       # variable de tipo Float
edad = 19           # variable de tipo Int

# Se muestran en pantalla las variables en uso
print()#el print por si solo genera un salto de linea

print("Nombre: ",nombre)
print("Altura: ",altura,"cm.")
print("Edad: ",edad,"años.")
print("Semestre:",semestre)

# Se modifican los valores de las variables y se mandan a imprimir
altura = 1.75
edad = 20
print()
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
# - Utilizar únicamente letras (mayúsculas o minúsculas), números y el guion bajo
# - La variable no puede iniciar con números
# - No se pueden utilizar palabras reservadas, ejemplos: if, else, True, class
# - Es sensible a mayúsculas y minúsculas. Por ejemplo, las palabras "Hola", "hola" y "HOLA"

# Buenas prácticas
# - Utilizar minúsculas para las palabras
# - Separar las palabras con el guion bajo
# - Utilizar nombres descriptivos de acuerdo a su uso. Por ejemplo: edad, en lugar de e..

# Ejemplos correctos y con buenas prácticas
fecha_nacimiento = "1 de enero del 2000"
clase = "Estructuras de Datos"
horas_estudio = 8
nombre = "Alberto"
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
