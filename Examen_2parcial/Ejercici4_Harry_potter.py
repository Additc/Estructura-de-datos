"""
Nombre: Addi Toro Chavez
Fecha: 7 de diciembre del 2024
Descripción:
Ejercicio 3  exámen, Sombrero seleccionador
"""
from random import choice
def menu():
    print()
    print("Test del sombrero seleccionador de Harry Potter")
    print("1) Iniciar test")
    print("2) Salir ")
    opcion=int(input("Ingrese una opcion: "))
    return opcion


def pregunta1(Diccionario_de_preguntas):
    print("¿Cuál de las siguientes opciones odiarías más que la gente te llamara?")
    contador = 0
    for pregunta in Diccionario_de_preguntas['pregunta1']:
        contador +=1
        print(f"{contador}) {pregunta}")
    opcion1 = int(input("Selecciona una opción :"))
    print()
    return opcion1

def pregunta2(Diccionario_de_preguntas):
    print("Después de tu muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?")
    contador = 0
    for pregunta in Diccionario_de_preguntas['pregunta2']:
        contador += 1
        print(f"{contador}) {pregunta}")
    opcion2 = int(input("Selecciona una opción :"))
    print()
    return opcion2

def pregunta3(Diccionario_de_preguntas):
    print("Dada la opción, preferirías inventar una poción que garantizara:")
    contador = 0
    for pregunta in Diccionario_de_preguntas['pregunta3']:
        contador += 1
        print(f"{contador}) {pregunta}")
    opcion3= int(input("Selecciona una opción :"))
    print()
    return opcion3

def pregunta4 (Diccionario_de_preguntas):
    print("¿Cómo te definirías en una sola palabra?")
    contador = 0
    for pregunta in Diccionario_de_preguntas['pregunta4']:
        contador += 1
        print(f"{contador}) {pregunta}")
    opcion4 = int(input("Selecciona una opción :"))
    print()
    return opcion4

def pregunta5 (Diccionario_de_preguntas):
    print("¿Qué cualidad te describe mejor?")
    contador=0
    for pregunta in Diccionario_de_preguntas['pregunta5']:
        contador+=1
        print(f"{contador}) {pregunta}")
    opcion5 = int(input("Selecciona una opción :"))
    print()
    return opcion5

def pregunta6 (Diccionario_de_preguntas):
    print("¿Cuál es tu clase favorita?")
    contador=0
    for pregunta in Diccionario_de_preguntas['pregunta6']:
        contador+=1
        print(f"{contador}) {pregunta}")
    opcion6 = int(input("Selecciona una opción :"))
    print()
    return opcion6

def pregunta7 (Diccionario_de_preguntas):
    print("¿Cuál es tu lenguaje de programación favorito?")
    contador=0
    for pregunta in Diccionario_de_preguntas['pregunta7']:
        contador += 1
        print(f"{contador}) {pregunta}")
    opcion7 = int(input("Selecciona una opción :"))
    print()
    return opcion7

def pregunta8 (Diccionario_de_preguntas):
    print("Elige un superpoder:")
    contador=0
    for pregunta in Diccionario_de_preguntas['pregunta8']:
        contador += 1
        print(f"{contador}) {pregunta}")
    opcion8 = int(input("Selecciona una opción :"))
    print()
    return opcion8

def test (Diccionario_de_preguntas):
    op1= 1
    op2= 1
    op3 =1
    op4 =1
    op5 =1
    op6 =1
    op7 =1
    op8=1

    Diccionario_de_casas = {'casa':["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw "]}

    # Para pregunta 1:
    while op1 != 0:
        op1 = pregunta1(Diccionario_de_preguntas)
        if op1>0 and op1<5:
            op1 = 0
        else:
            print("Error")
    # Para pregunta2
    while op2 != 0:
        op2 = pregunta2(Diccionario_de_preguntas)
        if op2>0 and op2<5:
            op2 = 0
        else:
            print("Error")
    # Para pregunta3
    while op3 != 0:
        op3 = pregunta3(Diccionario_de_preguntas)
        if op3>0 and op3<5:
            op3 = 0
        else:
            print("Error")
    # Para pregunta4
    while op4 != 0:
        opcion4 = pregunta4(Diccionario_de_preguntas)
        if op4>0 and op4<5:
            op4 = 0
        else:
            print("Error")
    # Para pregunta5
    while op5 != 0:
        op5 = pregunta5(Diccionario_de_preguntas)
        if op5>0 and op5<5:
            op5 = 0
        else:
            print("Error")
    # Para pregunta6
    while op6 != 0:
        op6 = pregunta6(Diccionario_de_preguntas)
        if op6>0 and op6<6:
            op6 = 0
        else:
            print("Error")
    # Para pregunta7
    while op7 != 0:
        op7 = pregunta7(Diccionario_de_preguntas)
        if op7>0 and op7<5:
            op7 = 0
        else:
            print("Error")
    while op8 != 0:
        op8 = pregunta8(Diccionario_de_preguntas)
        if op8>0 and op8<5:
            op8 = 0
        else:
            print("Error")

    # Elige una casa aleatoria
    casa = choice(Diccionario_de_casas['casa'])
    print(f"Tu casa es: {casa}")


Diccionario_de_preguntas = {'pregunta1': ("Ordinario", "Ignorante", "Cobarde", "Egoísta"),
                                'pregunta2': ("Te extraña pero sonríe", "Pide más historias sobre tus aventuras",
                                              "Piensa con admiración tus logros",
                                              "No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta."),
                                'pregunta3': ("Gloria", "Sabiduría", "Amor", "Poder"),
                                'pregunta4': ("Valiente", "Ambicioso", "Leal", "Curioso"),
                                'pregunta5': ("La fuerza", "La astucia", "La paciencia", "La inteligencia"),
                                'pregunta6': (
                                "Vuelo", "Defensa contra las artes oscuras", "Animales fantásticos", "Pociones"),
                                'pregunta7': ("C", "Python", "C++", "JavaScript"),
                                'pregunta8':("dormir","invisibilidad","superfuerza","teletransportarse")}

op = 1
while op != 0:
    opcion = menu()
    if opcion == 1:
        test(Diccionario_de_preguntas)
    elif opcion == 0:
        op = 0
        print("Salió del programa")
    else:
        print("opción incorrecta")