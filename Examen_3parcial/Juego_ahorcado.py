from random import random
import random


def menu ():
    """
    Menú que muestra el menú de opciones
    :return: La opción seleccionada por el usuario
    """
    print()
    print("Juego del ahorcado con animales")
    print("1) Jugar")
    print("0) Salir")
    opcion=(input("Teclea la opción que desea realizar: "))
    while not opcion.isnumeric():
        print("opción no válida")
        opcion= input("ingrese número nuevamente: ")
    opcion=int(opcion)
    return opcion


def obtener_palabra_aleatoria()->None:
    """
    Función que obtiene una palabra de un animal aleatorio
    :return: La palabra aleatoria obtenida
    """
    palabras=["tigre","leopardo","capibara","perro","armadillo","gato","serpiente","hormiga","pajaro",
              "ballena","leon","jirafa","pato","raton","conejo","aguila","orca","foca","pinguino","foca"]
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
                print("Felicidades, has acertado la palabra!")
                break
        else:
            intentos-=1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")
    if intentos == 0:
        print(f"Has perdido. La palabra secreta era: {palabra_secreta}")
        print()

if __name__ == '__main__':
    op=1
    while op!=0:
        opcion = menu()
        if opcion==1:
            jugar_ahorcado()
        elif opcion == 0:
            opcion = 0
            print("Salió del programa")
            break
        else:
            print("opcion incorrecta")

