"""
Nombre: Addi Toro Chavez
Fecha: 6 de noviembre del 2024
Descripción:
ciclo for
"""

#sintaxis
caracter=0
contador_caracteres=0
cadena_usuario= input("ingrese cadena: ")
for caracter in cadena_usuario:
    contador_caracteres +=1
    print(caracter, end ="-")

print()
print(f"el numero de caracteres es: {contador_caracteres}")
print()
#Ejercicio lista
#Imprime elementos individuales
alumno=0
alumnos=["Rosalinda","Juan","Loordes","Tania","Bryan","Rebeca","Jenni","Hector","Galilea","Patricia","Alberto","Addi"]
for alumno in alumnos:
    print(f"Hola {alumno}")
print()

for i in range(1,10):#funcion prestablecida que pide el inicio y el fin, y genera numeros del final -1
    print(i,end =",")
