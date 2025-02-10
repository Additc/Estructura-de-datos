'''
Nombre del equipo: Algoritmos anarquistas
Integrantes: Héctor Jésus Méndez Santiago, Jésus Alberto Ramírez Salinas y Addi Toro Chávez.
Fecha: 2 de febrero de 2025.
Descripción: Módulo corrspondiente al juego de 4 en rayas.
'''

import random


def menu_4_rayas() -> int:
    """
    Muestra el menú  del juego de Cuatro en Raya.
    """
    print()
    print("** Menú del juego 4 en raya**")
    print("1) Jugar contra otro jugador")
    print("2) Jugar contra la CPU")
    print("0) Salir")
    opcion = input("Seleccione una opción: ")
    while not opcion.isnumeric():
        print("opción no válida")
        opcion = input("Ingrese número nuevamente: ")
    opcion = int(opcion)
    return opcion

def mostrar_tablero(tablero: list) -> None:
    """
    Función que muestra el tablero del juego

    :param tablero: Lista como representación del tablero
    """
    print("\n")
    for fila in tablero:
        print(" | ".join(fila))  # El join es para unir una lista con sublistas
        print("-" * 29)
    print("\n")


def verificar_ganador(tablero: list, jugador: str) -> bool:
    """
    Función que verifica si el jugador ha ganado el juego.

    :param tablero: Representación del tablero
    :param jugador: Carácter de cada jugador X y O
    :return: True si en dado caso el jugador gana, o false si pierde
    """
    # Verificar filas
    for fila in tablero:
        for columna in range(4):
            if all(fila[columna + i] == jugador for i in
                   range(4)):  # Retorna verdadero si todos los elementos de la fila elinean cuatro elementos
                return True

    # Verificar columnas
    for columna in range(7):
        for fila in range(3):
            if all(tablero[fila + i][columna] == jugador for i in
                   range(4)):  # Retorna verdadero si todos los elementos en la columna alinean 4 elementos
                return True

    # Verificar diagonales de izquierda a derecha
    for fila in range(3):
        for columna in range(4):
            if all(tablero[fila + i][columna + i] == jugador for i in range(4)):
                return True

    # Verificar diagonales (de derecha a izquierda)
    for fila in range(3):
        for columna in range(3, 7):
            if all(tablero[fila + i][columna - i] == jugador for i in range(4)):
                return True

    return False


def columna_valida(tablero: list, columna: int) -> bool:
    """
    Función que verifica si una columna es válida para realizar un movimiento.

    :param tablero: Representación del tablero.
    :param columna: Número de columna .
    :return: True si la columna es válida, False en caso contrario.
    """
    return 0 <= columna < 7 and tablero[0][
        columna] == " "  # Retorna un valor en booleano, en este caso para verificar si la columna es válida pues debe cumplir que esté dentro del rango.


def realizar_movimiento(tablero: list, columna: int, jugador: str) -> None:
    """
    Función que realiza un movimiento en la columna deseada por el jugador.

    :param tablero:Representación del tablero.
    :param columna: Número de columna .
    :param jugador: Carácter que representa al jugador 'X'  o en caso contrario 'O'.
    """
    for fila in reversed(range(6)):
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            break


def movimiento_cpu(tablero: list) -> int:
    """
    Función que selecciona un lugar aleatorio para la CPU en el tablero.

    :param tablero: Lista bidimensional que representa el tablero.
    :return: Columna donde la CPU seleccionó el espacio.
    """
    columnas_validas = [columna for columna in range(7) if columna_valida(tablero, columna)]
    return random.choice(columnas_validas)


def jugar_contra_jugador() -> None:
    """
    Función que realiza el juego de cuatro en raya de jugador vs jugador.
    """
    tablero = [[" " for _ in range(7)] for _ in range(6)]
    mostrar_tablero(tablero)
    turno = "X"  # Jugador 1

    while True:
        print(f"Turno de {turno}")
        columna = input("Selecciona una columna entre 0 y 6: ")
        while not columna.isnumeric():
            print("opción no válida")
            columna = input("Ingrese número nuevamente una columna entre 0 y 6: ")
        columna= int(columna)

        while not columna_valida(tablero, columna):
            print("Columna inválida. Intenta de nuevo.")
            columna = int(input("Selecciona una columna entre 0 y 6: "))

        realizar_movimiento(tablero, columna, turno)
        mostrar_tablero(tablero)

        if verificar_ganador(tablero, turno):
            print()
            print(f" {turno} ha ganado!")
            break

        if all(tablero[0][col] != " " for col in range(7)):
            print()
            print("¡Empate!")
            break

        turno = "O" if turno == "X" else "X"  # Cambio de turno


def jugar_contra_cpu() -> None:
    """
    Función que inicia el juego de Cuatro en Raya contra la CPU.
    """
    tablero = [[" " for _ in range(7)] for _ in range(6)]
    mostrar_tablero(tablero)
    turno = "X"  # Jugador

    flag = 0
    while True:
        if turno == "X":
            print("Tu turno:")
            columna = input("Selecciona una columna entre 0 y 6): ")
            while not columna.isnumeric():
                print("opción no válida")
                columna = input("Ingrese número nuevamente una columna entre 0 y 6: ")
            columna = int(columna)

            while not columna_valida(tablero, columna):
                print("Columna inválida. Intenta de nuevo.")
                columna = int(input("Selecciona una columna entre 0 y 6): "))
        else:
            print("Turno de la CPU:")
            columna = movimiento_cpu(tablero)

        realizar_movimiento(tablero, columna, turno)
        mostrar_tablero(tablero)

        if verificar_ganador(tablero, turno):
            print(f"{turno} ha ganado!")
            flag = 1
            break

        if all(tablero[0][col] != " " for col in range(7)):
            print("¡Empate!")
            break

        turno = "O" if turno == "X" else "X"




def menu_principal_4rayas()->None:
    while True:
        opcion =menu_4_rayas()
        if opcion == 1:
            jugar_contra_jugador()
        elif opcion == 2:
            jugar_contra_cpu()
        elif opcion == 0:
            print("Salió del programa")
            break
        else:
            print("Acción incorrecta")

if __name__ == '__main__':
    menu_principal_4rayas()
