
import sys


matriz=[]
fila=0
columna=0
player1="O"
player2="X"


def menu ()->int:
    """
    Función que muestra el menú de opciones
    :return: Retorna la opción seleccionada por el usuario
    """
    print()
    print("Juego del gato")
    print("1) Jugar")
    print("0) Salir")
    opcion=(input("Teclea la opción que desea realizar: "))
    while not opcion.isnumeric():
        print("opción no válida")
        opcion= input("ingrese número nuevamente: ")
    opcion=int(opcion)
    return opcion



def tiros():
    """
    Función que muestra nuestra matriz inicial y además lleva el conteo de tiro que se llevan ejecutando
    :return: La función no retorna nada.
    """
    for i in range(3):
        matriz.append([" "] * 3)

    print("|", matriz[0][0], "|", matriz[0][1], "|", matriz[0][2], "|")
    print("_____________")
    print("|", matriz[1][0], "|", matriz[1][1], "|", matriz[1][2], "|")
    print("_____________")
    print("|", matriz[2][0], "|", matriz[2][1], "|", matriz[2][2], "|")
    coninuar=True
    tiros=0
    while coninuar:
        tiros+=1
        if (tiros%2==1):
            colocar_tablero("O")
        if (tiros%2==0):
            colocar_tablero("X")

        if (tiros==9):
            coninuar=False

def coordenada(nombre):
    """
    Función que válida los tiros dentro de nuestra matriz
    :param nombre: Hará la pregunta al usuario si es una fila o una columna
    :return: Retorna la coordenada
    """
    print(nombre)
    while True:
        cor=input()
        while (cor.isnumeric()==False):
            print("Digite un numero entre 0 y 2")
            cor=input()
        cor=int(cor)
        if(cor>=0 and cor<=2):
            return cor

def colocar_tablero(jugador):
    """
    Función que solicita la pocisión en la que el jugador desea colocar su ficha, además validando que
    que no se pueda seleccionar la misma casilla
    :param jugador:
    :return: No retorna nada solo muestra el progreso del juego
    """
    fila=coordenada("Ingrese fila: ")
    columna=coordenada("Ingrese columna: ")
    if matriz[fila][columna]=="O":
        print("La pocision ya esta ocupada")
        fila = coordenada("Ingrese nuevamente fila: ")
        columna=coordenada("Ingrese nuevamente columna: ")

    if matriz[fila][columna]=="X":
        print("La pocision ya esta ocupada")
        fila=coordenada("Ingrese nuevamente fila: ")
        columna = coordenada("Ingrese nuevamente columna: ")

    matriz[fila][columna]=jugador
    print(estado_juego(matriz))
    print("|", matriz[0][0], "|", matriz[0][1], "|", matriz[00][2], "|")
    print("_____________")
    print("|", matriz[1][0], "|", matriz[1][1], "|", matriz[1][2], "|")
    print("_____________")
    print("|", matriz[2][0], "|", matriz[2][1], "|", matriz[2][2], "|")
    print("_____________")

def estado_juego(matriz):
    """
    Función que hace validar al ganador del juego, dependiendo del estado actual
    :param matriz: Es la matriz validando lo casos para ganar dentro del juego
    :return: Ganador del juego
    """
    #lineas horizontales
    if ("O"==matriz[0][0]==matriz[0][1]==matriz[0][2] != ' '):
        estado_actual="Ganador jugador 1"
        ganador(estado_actual)
    if ("O"==matriz[1][0]==matriz[1][1]==matriz[1][2] != ' '):
        estado_actual="Ganador jugador 1"
        ganador(estado_actual)
    if ("O"==matriz[2][0]==matriz[2][1]==matriz[2][2] != ' '):
        estado_actual="Ganador jugador 1"
        ganador(estado_actual)

    if ("X"==matriz[0][0]==matriz[0][1]==matriz[0][2] != ' '):
        estado_actual="Ganador jugador 2"
        ganador(estado_actual)
    if ("X"==matriz[1][0]==matriz[1][1]==matriz[1][2] != ' '):
        estado_actual="Ganador jugador 2"
        ganador(estado_actual)
    if ("X"==matriz[2][0]==matriz[2][1]==matriz[2][2] != ' '):
        estado_actual="Ganador jugador 2"
        ganador(estado_actual)

    #lineas verticales
    if ("O"==matriz[0][0]==matriz[1][0]==matriz[2][0] != ' '):
        estado_actual="Ganador jugador 1"
        ganador(estado_actual)
    if ("O"==matriz[0][1]==matriz[1][1]==matriz[2][1] != ' '):
        estado_actual="Ganador jugador 1"
        ganador(estado_actual)
    if ("O"==matriz[0][2]==matriz[1][2]==matriz[2][2] != ' '):
        estado_actual="Ganador jugador 1"
        ganador(estado_actual)

    if ("X"==matriz[0][0]==matriz[1][0]==matriz[2][0] != ' '):
        estado_actual="Ganador jugador 2"
        ganador(estado_actual)
    if ("X"==matriz[0][1]==matriz[1][1]==matriz[2][1] != ' '):
        estado_actual="Ganador jugador 2"
        ganador(estado_actual)
    if ("X"==matriz[0][2]==matriz[1][2]==matriz[2][2] != ' '):
        estado_actual="Ganador jugador 2"
        ganador(estado_actual)


    #lineas diagonales
    if ("O"==matriz[0][0]==matriz[1][1]==matriz[2][2] != ' '):
        estado_actual="Ganador jugador 1"
        ganador(estado_actual)
    if ("O"==matriz[0][2]==matriz[1][1]==matriz[2][0] != ' '):
        estado_actual="Ganador jugador 1 "
        ganador(estado_actual)

    if ("X"==matriz[0][0]==matriz[1][1]==matriz[2][2] != ' '):
        estado_actual="Ganador jugador 2"
        ganador(estado_actual)
    if ("X"==matriz[0][2]==matriz[1][1]==matriz[2][0] != ' '):
        estado_actual="Ganador jugador 2"
        ganador(estado_actual)

def ganador(estado_actual):
        """
        Función que muestra al ganador del juego y el resultado dentro de la matriz
        :param estado_actual:
        :return:
        """
        print()
        print(estado_actual)
        print("|", matriz[0][0], "|", matriz[0][1], "|", matriz[0][2], "|")
        print("_____________")
        print("|", matriz[1][0], "|", matriz[1][1], "|", matriz[1][2], "|")
        print("_____________")
        print("|", matriz[2][0], "|", matriz[2][1], "|", matriz[2][2], "|")
        print("_____________")
        sys.exit(0)

if __name__ == '__main__':
    op=1
    while op!=0:
        opcion = menu()
        if opcion==1:
            tiros()
        elif opcion == 0:
            opcion = 0
            print("Salió del programa")
            break
        else:
            print("opcion incorrecta")