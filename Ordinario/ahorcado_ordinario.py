'''
Nombre del equipo: Algoritmos anarquistas
Integrantes: Héctor Jésus Méndez Santiago, Jésus Alberto Ramírez Salinas y Addi Toro Chávez.
Fecha: 2 de febrero de 2025.
Descripción: Módulo correspondiente al juego del ahorcado.
'''

from random import random
import random


def menu_ahorcado():
    """
    Menú que muestra el menú de opciones
    :return: La opción seleccionada por el usuario
    """
    print()
    print("Juego del ahorcado")
    print("1) Jugar")
    print("0) Salir")
    opcion=(input("Teclea la opción que desea realizar: "))
    while not opcion.isnumeric():
        print("opción no válida")
        opcion= input("ingrese número nuevamente: ")
    opcion=int(opcion)
    return opcion


def dibujos(bandera) -> None:
    """
    Dibuja las diferentes etapas del ahorcado según el número de errores
    :param bandera: Número que indica en qué etapa del juego estamos
    :return: No retorna nada
    """
    if bandera == 1:
        print("  _______     ")
        print(" |/      |     ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    elif bandera == 2:
        print("  _______     ")
        print(" |/      |     ")
        print(" |      O     ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    elif bandera == 3:
        print("  _______     ")
        print(" |/      |     ")
        print(" |      O     ")
        print(" |     /|\    ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    elif bandera == 4:
        print("  _______     ")
        print(" |/      |     ")
        print(" |      O     ")
        print(" |     /|\    ")
        print(" |      |     ")
        print(" |            ")
        print("_|___         ")
    elif bandera == 5:
        print("  _______     ")
        print(" |/      |     ")
        print(" |      O     ")
        print(" |     /|\    ")
        print(" |      |      ")
        print(" |     /       ")
        print("_|___         ")
    else:
        print("  _______     ")
        print(" |/      |     ")
        print(" |      O     ")
        print(" |     /|\    ")
        print(" |      |      ")
        print(" |     / \     ")
        print("_|___         ")

        print("\nTus vidas se acabaron.")


def obtener_palabra_aleatoria()->None:
    """
    Función que obtiene una palabra de un animal aleatorio
    :return: La palabra aleatoria obtenida
    """
    palabras=["mouse","teclado","computadora","programar","botella","gato","amarillo","espejo","ventana",
              "ballena","leon","sillon","paraguas","luna","estrella","pelota","cama","rojo","cielo","regla"]
    palabra_aleatoria=random.choice(palabras)
    return palabra_aleatoria

def mostrar_palabra(palabra_secreta, letras_adivinadas):
    """
    Función que muestra al usuario los espacios de la palabra aleatoria obtenida
    :param palabra_secreta: palabra del animal seleccionado aleatoriamente
    :param letras_adivinadas: Letras acertadas por el usuario
    :return: Muestra los espacios de las palabra a adivinar
    """
    tablero=""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero+=letra
        else:
            tablero+="_"
    print(tablero)

def jugar_ahorcado():
    """
    Función que valida que se ingrese una letra, además de que esta no sea repetida, y también
    muestra si la palabra ha sido adivinada o en su dado caso ah perdido el juego.
    :return:
    """
    palabra_secreta=obtener_palabra_aleatoria()
    letras_adivinadas=[]
    intentos=5
    bandera=1
    bandera2=1
    errores=1

    dibujos(bandera)
    while intentos>0:
        mostrar_palabra(palabra_secreta,letras_adivinadas)
        letra=input("Ingrese una letra: " )
        while letra.isnumeric():
            print("opción no válida")
            letra= input("Ingrese letra nuevamente: ")
        letra= str(letra)

        if letra in letras_adivinadas:
             print("Ya has introducida esa letra. Puebra con otra")
             continue

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            if set(letras_adivinadas) == set(palabra_secreta):
                print(f"Felicidades, has acertado la palabra!, la palabra era {palabra_secreta}")
                break
        else:
            intentos-=1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")
            if intentos == 4:
                bandera=2
                dibujos(bandera)
            if intentos == 3:
                bandera=3
                dibujos(bandera)
            if intentos == 2:
                bandera=4
                dibujos(bandera)
            if intentos == 1:
                bandera=5
                dibujos(bandera)
            if intentos == 0:
                bandera=6
                dibujos(bandera)
                print(f"Has perdido. La palabra secreta era: {palabra_secreta}")
                print()

def menu_principal_ahorcado()->None:
    op=1
    while op!=0:
        opcion = menu_ahorcado()
        if opcion==1:
            jugar_ahorcado()
        elif opcion == 0:
            opcion = 0
            print("Salió del programa")
            break
        else:
            print("opcion incorrecta")

if __name__ == '__main__':
    menu_principal_ahorcado()