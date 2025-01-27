
from colorama import init, Fore, Style
import random
from copy import deepcopy

minimo_fila= 5
maximo_filas = 10
minimo_columnas = 6
maximo_columnas = 10
espacio_vacio= " "
color_1 = "x"
color_2 = "o"
jugador_1 = 1
# La CPU también es el jugador 2
jugador_2 = 2
conecta = 4
esta_jugando_CPU = False


def solicitar_numero():
    while True:
        try:
            posible_entero=int(input("Ingrese numero de columna: "))
            return posible_entero
        except ValueError:
            continue

def cadena_a_entero (cadena:str)->int|None:
    no_guiones=cadena.count("-")
    revisar_cadena=cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0,1):
        return int(cadena)
    else:
        return None

def solicitar_columnas():
    while True:
        columnas=input("Ingrese numero de columnas: ")
        numero_columnas= cadena_a_entero(columnas)
        while numero_columnas is None:
            columnas = input("opcion invalida, intente nuevamente: ")
            numero_columnas = cadena_a_entero(columnas)
        if numero_columnas < minimo_columnas or numero_columnas > maximo_columnas:
            print(f"El numero minimo de columnas es {minimo_columnas} y el maximo {maximo_columnas}")
        else:
            return numero_columnas

def solicitar_filas():
    while True:
        filas=input("Ingrese numero de filas: ")
        numero_filas= cadena_a_entero(filas)
        while numero_filas is None:
            filas = input("opcion invalida, intente nuevamente: ")
            numero_filas = cadena_a_entero(filas)
        if numero_filas < minimo_columnas or numero_filas > maximo_columnas:
            print(f"El numero minimo de columnas es {minimo_columnas} y el maximo {maximo_columnas}")
        else:
            return numero_filas


def crear_tablero(filas, columnas):
    tablero = []
    for fila in range(filas):
        tablero.append([])
        for columna in range(columnas):
            tablero[fila].append(espacio_vacio)
    return tablero


def imprimir_tablero(tablero):
    # Imprime números de columnas
    print("|", end="")
    for f in range(1, len(tablero[0]) + 1):
        print(f, end="|")
    print("")
    # Datos
    for fila in tablero:
        print("|", end="")
        for valor in fila:
            color_terminal = Fore.GREEN
            if valor == color_2:
                color_terminal = Fore.RED
            print(color_terminal + valor, end="")
            print(Style.RESET_ALL, end="")
            print("|", end="")
        print("")
    # Pie
    print("+", end="")
    for f in range(1, len(tablero[0]) + 1):
        print("-", end="+")
    print("")

def obtener_fila_valida_en_columna(columna, tablero):
    indice = len(tablero) - 1
    while indice >= 0:
        if tablero[indice][columna] == espacio_vacio:
            return indice
        indice -= 1
    return -1

def solicitar_columna(tablero):
    """
    Solicita la columna y devuelve la columna ingresada -1 para ser usada fácilmente como índice
    """
    while True:
        columna = input("Ingresa la columna para colocar la pieza: ")
        columna_seleccionada = cadena_a_entero(columna)
        while columna_seleccionada is None:
            columna = input("opcion invalida, intente nuevamente: ")
            columna_seleccionada = cadena_a_entero(columna)
        if columna_seleccionada <= 0 or columna_seleccionada > len(tablero[0]):
            print("Columna no válida")
        elif tablero[0][columna_seleccionada - 1] != espacio_vacio:
            print("Esa columna ya está llena")
        else:
            return columna_seleccionada - 1


def colocar_pieza(columna, jugador, tablero):
    """
    Coloca una pieza en el tablero. La columna debe
    comenzar en 0
    """
    color = color_1
    if jugador == jugador_2:
        color = color_2
    fila = (columna, tablero)
    if fila == -1:
        return False
    tablero[fila][columna] = color
    return True

def obtener_conteo_derecha(fila, columna, color, tablero):
    fin_columnas = len(tablero[0])
    contador = 0
    for i in range(columna, fin_columnas):
        if contador >= conecta:
            return contador
        if tablero[fila][i] == color:
            contador += 1
        else:
            contador = 0
    return contador


def obtener_conteo_izquierda(fila, columna, color, tablero):
    contador = 0
    # -1 porque no es inclusivo
    for i in range(columna, -1, -1):
        if contador >= conecta:
            return contador
        if tablero[fila][i] == color:
            contador += 1
        else:
            contador = 0

    return contador


def obtener_conteo_abajo(fila, columna, color, tablero):
    fin_filas = len(tablero)
    contador = 0
    for i in range(fila, fin_filas):
        if contador >= conecta:
            return contador
        if tablero[i][columna] == color:
            contador += 1
        else:
            contador = 0
    return contador


def obtener_conteo_arriba(fila, columna, color, tablero):
    contador = 0
    for i in range(fila, -1, -1):
        if contador >= conecta:
            return contador
        if contador >= conecta:
            return contador
        if tablero[i][columna] == color:
            contador += 1
        else:
            contador = 0
    return contador


def obtener_conteo_arriba_derecha(fila, columna, color, tablero):
    contador = 0
    numero_fila = fila
    numero_columna = columna
    while numero_fila >= 0 and numero_columna < len(tablero[0]):
        if contador >= conecta:
            return contador
        if tablero[numero_fila][numero_columna] == color:
            contador += 1
        else:
            contador = 0
        numero_fila -= 1
        numero_columna += 1
    return contador


def obtener_conteo_arriba_izquierda(fila, columna, color, tablero):
    contador = 0
    numero_fila = fila
    numero_columna = columna
    while numero_fila >= 0 and numero_columna >= 0:
        if contador >= conecta:
            return contador
        if tablero[numero_fila][numero_columna] == color:
            contador += 1
        else:
            contador = 0
        numero_fila -= 1
        numero_columna -= 1
    return contador


def obtener_conteo_abajo_izquierda(fila, columna, color, tablero):
    contador = 0
    numero_fila = fila
    numero_columna = columna
    while numero_fila < len(tablero) and numero_columna >= 0:
        if contador >= conecta:
            return contador
        if tablero[numero_fila][numero_columna] == color:
            contador += 1
        else:
            contador = 0
        numero_fila += 1
        numero_columna -= 1
    return contador


def obtener_conteo_abajo_derecha(fila, columna, color, tablero):
    contador = 0
    numero_fila = fila
    numero_columna = columna
    while numero_fila < len(tablero) and numero_columna < len(tablero[0]):
        if contador >= conecta:
            return contador
        if tablero[numero_fila][numero_columna] == color:
            contador += 1
        else:
            contador = 0
        numero_fila += 1
        numero_columna += 1
    return contador


def obtener_direcciones():
    return [
        'izquierda',
        'arriba',
        'abajo',
        'derecha',
        'arriba_derecha',
        'abajo_derecha',
        'arriba_izquierda',
        'abajo_izquierda',
    ]


def obtener_conteo(fila, columna, color, tablero):
    direcciones = obtener_direcciones()
    for direccion in direcciones:
        funcion = globals()['obtener_conteo_' + direccion]
        conteo = funcion(fila, columna, color, tablero)
        if conteo >= conteo:
            return conteo
    return 0

