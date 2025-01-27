"""
Nombre: Addi Toro Chavez
Fecha: 7 de diciembre del 2024
Descripción:
Ejercicio 3  exámen, Lenguaje Hacker
"""
#Definción del menú de opciones para la conversión del lenguaje Hacker
def menu():
    print()
    print("Lenguaje Hacker")
    print("Selecciones una opción: ")
    print("1) Convertir un texto a lenguaje l33t básico")
    print("2) Convertir un texto a lenguaje l33t intermedio")
    print("3) Salir")
#Se obtiene la opción seleccionada
    opcion=int(input("Ingrese una opción: "))
    return opcion

#Definición de la función para obtener la conversión del lenguaje l33t básico
def basico():
# variable que almacenará las letras
    texto_2=" "
#Se define un diccionario con las vocales minúsculas y mayúsculas con sus definción de este lenguaje
    vocales={'a':"4",'e':"3",'i':"1",'o':"0",'u':"(_)",'A':"4",'E':"3",'I':"1",'O':"0",'U':"(_)",
             '0':"o",'1':"L",'2':"R",'3':"E",'4':"A",'5':"S",'6':"b",'7':"T",'8':"B",'9':"g"}
#Solicitamos el texto a convertir, al usuario.
    texto=input("Ingrese el texto a convertir en lenguaje l33t básico: ")
#Inplementación de la lógica para encontrar un vocal dentro del texto ingresado y ser remplazado por su definición de lenguaje l33t
    print("El texto convertido es: ")
    for i in texto:
        texto_2=[i]
        if i in vocales:
            texto_2=vocales[i]
            print(texto_2,end=" ")
        else:
            texto_2=i
            print(texto_2, end=" ")
    print()

#Definición de la función para obtener la conversión del lenguaje l33t intermedio
def intermedio ():
# variable que almacenará las letras
    texto_2=" "
#Se define un diccionario que almacena el abecedario en minúsculas y mayúsculas con sus definción en este lenguaje l33t
    vocales = {'a': "4", 'b': "|3", 'c': "[", 'd': ")", 'e': "3", 'f': "|=", 'g': "&", 'h': "#", 'i': "1", 'j': ",_|",
               'k': ">|", 'l': "1", 'm': "^^", 'n':"|\|", 'o': "0", 'p': "|*", 'q': "(_,)", 'r': "12", 's': "5", 't': "7",
               'u': "(_)", 'v': "\/", 'w': "\/\/", 'x': "><", 'y': "j", 'z': "2",
               'A': "4", 'B': "|3", 'C': "[", 'D': ")", 'E': "3", 'F': "|=", 'G': "&", 'H': "#", 'I': "1", 'J': ",_|",
               'K': ">|", 'L': "1", 'M': "^^", 'N': "|\|", 'O': "0", 'P': "|*", 'Q': "(_,)", 'R': "12", 'S': "5",'T': "7",
               'U': "(_)", 'V': "\/", 'W': "\/\/", 'X': "><", 'Y': "j", 'Z': "2",
                '0':"o",'1':"L",'2':"R",'3':"E",'4':"A",'5':"S",'6':"b",'7':"T",'8':"B",'9':"g"
               }
#Solicitamos el texto a convertir, al usuario.
    texto = input("Ingrese el texto a convertir en lenguaje l33t intermedio: ")
#Inplementación de la lógica para encontrar un vocal dentro del texto ingresado y ser remplazado por su definición de lenguaje l33t
    print("El texto convertido es: ")
    for i in texto:
        texto_2 = [i]
        if i in vocales:
            texto_2 = vocales[i]
            print(texto_2, end=" ")
        if i == " ":
            print(" ", end=" ")

    print()

#Declración de mi ciclo while, estableciendo la condiciones según sea la opción seleccionada por el usuario, y realizando una llamada de,
# la función según corresponda.
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