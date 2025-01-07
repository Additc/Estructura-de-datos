'''
Nombre: Addi Toro Chavez
Fecha: 7 de enero de 2025.
Descripción: verificar entrada consola.
'''
prueba_numero=int(input("ingrese número: "))
print()

#funciones con cadenas que nos van a servir
cadena=input("ingrese cadena: ")
print(cadena.isnumeric())
print()
print(cadena.isalpha())
print()
print(cadena.isalnum())
print()

numero=input("ingresa número: ")#valor string o cadena
while not numero.isnumeric():
    print("opción no válida")
    numero=input("ingrese número nuevamente: ")
print()
numero=int(numero)#verifica si es un número
print(f"El número {numero} es de tipo {type(numero)}")#type para saber el tipo de dato



#Ahora con todos los números negativos
def cadena_a_entero (cadena):
    no_guiones=cadena.count("-")
    revisar_cadena=cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0,1):
        return int(cadena)
    else:
        return None
print()

num_cadena=input("ingrese z: ")
numero=cadena_a_entero(num_cadena)
while numero is None:
    print("opción inválida")
    num_cadena=input("ingrese nuevamente: ")
    numero=cadena_a_entero(num_cadena)
print(f"El número {numero} es de tipo {type(numero)}")#type para saber el tipo de dato


#Ahora con todos los números decimales
def cadena_a_flotante (cadena):
    no_puntos=cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".")
    if revisar_cadena.isnumeric() and no_puntos in (0,1):
        return float(cadena)
    else:
        return None
print()

num_cadena=input("ingrese z: ")
numero=cadena_a_entero(num_cadena)
while numero is None:
    print("opción inválida")
    num_cadena=input("ingrese nuevamente: ")
    numero=cadena_a_entero(num_cadena)
print(f"El número {numero} es de tipo {type(numero)}")#type para saber el tipo de dato