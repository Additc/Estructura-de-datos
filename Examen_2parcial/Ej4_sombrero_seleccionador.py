"""
Nombre: Addi Toro Chavez
Fecha: 7 de diciembre del 2024
Descripción:
Ejercicio 3  exámen, Sombrero seleccionador
"""
def menu():
    print("Test del sombrero seleccionador de Harry Potter")
    print("1) Iniciar test")
    print("2) Salir ")
    opcion=int(input("Ingrese una opcion: "))
    return opcion

def test():
    Diccionario_de_preguntas = {'pregunta1': ("Ordinario", "Ignorante", "Cobarde", "Egoísta"),
                                'pregunta2': ("Te extraña pero sonríe", "Pide más historias sobre tus aventuras",
                                              "Piensa con admiración tus logros",
                                              "No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta."),
                                'pregunta3': ("Gloria", "Sabiduría", "Amor", "Poder"),
                                'pregunta4': ("Valiente", "Ambicioso", "Leal", "Curioso"),
                                'pregunta5': ("La fuerza", "La astucia", "La paciencia", "La inteligencia"),
                                'pregunta6': (
                                "Vuelo", "Defensa contra las artes oscuras", "Animales fantásticos", "Pociones"),
                                'pregunta7': ("C", "Python", "C++", "JavaScript")}

    print("¿Cuál de las siguientes opciones odiarías más que la gente te llamara?")
    contador = 0
    # Muestra las opciones
    for pregunta in Diccionario_de_preguntas['pregunta1']:
        contador +=1
        print(f"{contador}) {pregunta}")
    # Lectura de datos
    opcion = int(input("\nSelecciona una opción :"))

    print("Después de tu muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?")
    contador = 0
    for pregunta in Diccionario_de_preguntas['pregunta2']:
        contador += 1
        print(f"{contador}) {pregunta}")
    opcion2 = int(input("\nSelecciona una opción :"))

    print("Dada la opción, preferirías inventar una poción que garantizara:")
    contador = 0
    for pregunta in Diccionario_de_preguntas['pregunta3']:
        contador += 1
        print(f"{contador}) {pregunta}")
    opcion3= int(input("\nSelecciona una opción :"))


op = 1
while op != 0:
    opcion = menu()
    if opcion == 1:
        test()
    elif opcion == 0:
        op = 0
        print("Salió del programa")
    else:
        print("opción incorrecta")