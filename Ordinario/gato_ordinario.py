'''
Nombre del equipo: Algoritmos anarquistas
Integrantes: Héctor Jésus Méndez Santiago, Jésus Alberto Ramírez Salinas y Addi Toro Chávez.
Fecha: 2 de febrero de 2025.
Descripción: Módulo correspondiente al juego del gato.
'''

import random
from time import sleep

from colorama import init


init()
def menu_gato()->int:
    print()
    print("** Menú del juego Gato**")
    print("1.- Jugar 1 vs 1.")
    print("2.- Jugar 1 vs CPU.")

    print("0.- Salir.")
    opcion = input("Escoja una opción: ")
    while not opcion.isnumeric():
        print("Opción no válida")
        opcion = input("Intenta nuevamente: ")
    opcion = int(opcion)
    print()
    return opcion



def imprimir_tablero(tablero)->None:
    """
    Función que imprime el tablero del gato.
    :param tablero: Matriz del juego del gato.
    :return:
    """
    print("-------------")
    for fila in tablero:
        print("|", fila[0], "|", fila[1], "|", fila[2], "|")
        print("-------------")


def ganador(tablero, jugador:str)->bool:
    """
    Función que determina al ganador de la partida.
    :param tablero: Matriz de 3x3.
    :param jugador: Jugador o CPU.
    :return:
    """
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

def limpiar_tablero(tablero)->None:
    for i in range(3):
        for j in range(3):
            tablero[i][j] = ' '


def empate(tablero)->bool:
    """
    Función que determina si el tablero está lleno.
    :param tablero: Matriz de 3x3.
    :return:
    """
    for fila in tablero:
        if ' ' in fila:
            return False
    return True

def unovscpu(tablero)->None:
    """
    Función que nos permite jugar el juego del gato.
    :param tablero: Matriz de 3x3.
    :return:
    """
    limpiar_tablero(tablero)
    jugador = "x"
    cpu = "o"

    while True:
        imprimir_tablero(tablero)
        valido = False
        while not valido:
            print("Turno del jugador: x")
            fila = input("Escoge una fila (0,1,2): ")
            columna = input("Escoge una columna (0,1,2): ")
            if not (fila.isnumeric() and columna.isnumeric()):
                print("Opción no válida. Ingresa números.")
            else:
                fila, columna = int(fila), int(columna)

                if fila < 0 or fila > 2 or columna < 0 or columna > 2:
                    print("Opción fuera de rango. Inténtalo de nuevo.")
                elif tablero[fila][columna] == " ":
                    tablero[fila][columna] = jugador
                    valido = True
                else:
                    print("Lugar ocupado.")

        if ganador(tablero, jugador):
            imprimir_tablero(tablero)
            print("Felicidades!, has ganado el juego.")
            break

        if empate(tablero):
            imprimir_tablero(tablero)
            print("Es un empate.")
            break

        valido_cpu = False
        while not valido_cpu:
            fila_cpu = random.randint(0, 2)
            columna_cpu = random.randint(0, 2)
            if tablero[fila_cpu][columna_cpu] == " ":
                tablero[fila_cpu][columna_cpu] = cpu
                valido_cpu = True

        if ganador(tablero, cpu):
            imprimir_tablero(tablero)
            print("Gano la CPU, suerte a la próxima.")
            break

        if empate(tablero):
            imprimir_tablero(tablero)
            print("Es un empate.")
            break

def unovsuno(tablero)->None:
    jugador1 = "x"
    jugador2 = "o"
    limpiar_tablero(tablero)

    while True:
        imprimir_tablero(tablero)
        valido = False
        while not valido:
            print(f"Jugador 1 {jugador1}")
            fila = input("Escoge una fila (0,1,2): ")
            columna = input("Escoge una columna (0,1,2): ")
            if not (fila.isnumeric() and columna.isnumeric()):
                print("Opción no válida. Ingresa números.")
            else:
                fila, columna = int(fila), int(columna)

                if fila < 0 or fila > 2 or columna < 0 or columna > 2:
                    print("Opción fuera de rango. Inténtalo de nuevo.")
                elif tablero[fila][columna] == " ":
                    tablero[fila][columna] = jugador1
                    valido = True
                else:
                    print("Lugar ocupado.")

        if ganador(tablero, jugador1):
            imprimir_tablero(tablero)
            print("Felicidades!, ha ganado el jugador 1 x.")
            break

        if empate(tablero):
            imprimir_tablero(tablero)
            print("Es un empate.")
            break

        imprimir_tablero(tablero)
        valido_j2 = False
        while not valido_j2:
            print(f"Jugador 2 {jugador2}")
            fila = input("Escoge una fila (0,1,2): ")
            columna = input("Escoge una columna (0,1,2): ")
            if not (fila.isnumeric() and columna.isnumeric()):
                print("Opción no válida. Ingresa números.")
            else:
                fila, columna = int(fila), int(columna)

                if fila < 0 or fila > 2 or columna < 0 or columna > 2:
                    print("Opción fuera de rango. Inténtalo de nuevo.")
                elif tablero[fila][columna] == " ":
                    tablero[fila][columna] = jugador2
                    valido_j2 = True
                else:
                    print("Lugar ocupado.")

        if ganador(tablero, jugador2):
            imprimir_tablero(tablero)
            print("Felicidades!, ha ganado el jugador 2 o.")
            break

        if empate(tablero):
            imprimir_tablero(tablero)
            print("Es un empate.")
            break

def menu_principal_gatos()->None:
    tablero = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    while True:
        opcion = menu_gato()
        if opcion == 1:
            unovsuno(tablero)
        elif opcion == 2:
            unovscpu(tablero)
        elif opcion == 0:
            print("Vuelve pronto.")
            break
        else:
            print("Valor no válido.")

if __name__ == '__main__':
    menu_principal_gatos()