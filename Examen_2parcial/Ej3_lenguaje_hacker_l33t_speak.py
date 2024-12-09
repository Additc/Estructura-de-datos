"""
Nombre: Addi Toro Chavez
Fecha: 7 de diciembre del 2024
Descripción:
Ejercicio 3  exámen, Lenguaje Hacker
"""

def menu():
    print()
    print("Selecciones una opción: ")
    print("1) Convertir un texto a lenguaje básico")
    print("2) Convertir un texto a lenguaje intermedio")
    print("3) Salir")
    opcion=int(input("Ingrese una opción: "))
    return opcion

def basico():
    texto_2=" "
    vocales={'a':"4",'e':"3",'i':"1",'o':"0",'u':"(_)",'A':"4",'E':"3",'I':"1",'O':"0",'U':"(_)"}
    texto=input("Ingrese el texto a convertir en lenguaje l33t básico: ")
    print("El texto invertido es: ")
    for i in texto:
        texto_2=[i]
        if i in vocales:
            texto_2=vocales[i]
            print(texto_2,end=" ")
        else:
            texto_2=i
            print(texto_2, end=" ")
    print()

def intermedio ():
    texto_2=" "
    vocales = {'a': "4", 'b': "|3", 'c': "[", 'd': ")", 'e': "3", 'f': "|=", 'g': "&", 'h': "#", 'i': "1", 'j': ",_|",
               'k': ">|", 'l': "1", 'm': "^^", 'n':"|\|", 'o': "0", 'p': "|*", 'q': "(_,)", 'r': "12", 's': "5", 't': "7",
               'u': "(_)", 'v': "\/", 'w': "\/\/", 'x': "><", 'y': "j", 'z': "2",
               'A': "4", 'B': "|3", 'C': "[", 'D': ")", 'E': "3", 'F': "|=", 'G': "&", 'H': "#", 'I': "1", 'J': ",_|",
               'K': ">|", 'L': "1", 'M': "^^", 'N': "|\|", 'O': "0", 'P': "|*", 'Q': "(_,)", 'R': "12", 'S': "5",'T': "7",
               'U': "(_)", 'V': "\/", 'W': "\/\/", 'X': "><", 'Y': "j", 'Z': "2"
               }
    texto = input("Ingrese el texto a convertir en lenguaje l33t intermedio: ")
    print("El texto invertido es: ")
    for i in texto:
        texto_2 = [i]
        if i in vocales:
            texto_2 = vocales[i]
            print(texto_2, end=" ")
        if i == " ":
            print(" ", end=" ")

    print()
op = 1
while op != 0:
    opcion = menu()
    if opcion == 1:
        basico()
    elif opcion == 2:
        intermedio()
    elif opcion == 0:
        op = 0
        print("Salió del programa")
    else:
        print("opción incorrecta")