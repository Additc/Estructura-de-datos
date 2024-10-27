'''
Addi Toro Chavez
27 de octubre de 2024.
Descripción:
Ejercicio número 3 de operadores en python

Descripcion:
Este programa determinará si un usuario se autentifica correctamente con su usuario y contraseña. Para ello:
a) Internamente declare dos cadenas constantes, una para el usuario y otra para la contraseña.
b) Pida al usuario una cadena con el usuario.
c) Pida al usuario una cadena con la contraseña.
d) Si ambas cadenas son iguales a las cadenas declaradas internamente, entonces el usario se autenticó correctamente.
e) Muestre el resultado en consola como valor booleano (True/False).

Nota: Las cadenas no tiene que ser convertidas a minúsculas.
'''

#Declaramos las 2 cadenas internamente.
usuario="Addi"
contraseña="2005"
# Pedimos al usuario que ingrese los datos.
usuario2=input("ingrese el nombre de usuario: ")
contraseña2=input("ingrese su contraseña: ")

# Realizamos la comparación y mostramos en pantalla.
print(f"El acceso es correcto: {usuario==usuario2 and contraseña==contraseña2}")

