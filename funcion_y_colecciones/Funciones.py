"""
Nombre: Addi Toro Chavez
Fecha: 6 de noviembre del 2024
Descripción:
Llamada de funciones
"""



#Declaración de función
def hola(nombre):
    print(f"Hola {nombre}")

#llamada de la función
nombre=input("Ingresa nombre:")
#Mandar a la función
hola(nombre)
print("Adios")

#Función de menú
def menu( ):
    print("Ingrese una opción:")
    print("1: suma")
    print("2: resta")
    print("3: multiplicación")
    print("4: división")
    print("5: división entrera")
    print("6: módulo")
    print("7: potenciación")
    opcion=int(input("Ingrese la opción: "))
    return opcion
opcion=menu()

def calculadora(opcion,num_1,num_2):
    if opcion==1:
        resultado= num_1+num_2
    elif opcion==2:
        resultado = num_1-num_2
    elif opcion==3:
        resultado = num_1*num_2
    elif opcion==4:
        resultado = num_1/num_2
    elif opcion==5:
        resultado = num_1//num_2
    elif opcion==6:
        resultado = num_1%num_2
    elif opcion==7:
        resultado = num_1**num_2

    return resultado

num_1=float(input("ingrese el primer numero: "))
num_2=float(input("ingrese el segundo numero: "))
resultado=(calculadora(opcion,num_1,num_2))
print(f"El resultado es: {(resultado):.3f}")


