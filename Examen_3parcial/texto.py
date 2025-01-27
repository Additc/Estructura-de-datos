import sys
import time
from colorama import Fore, init

# Inicializa colorama
init(autoreset=True)

def animacion_texto(texto, velocidad=0.1, color=Fore.RED):
    for letra in texto:
        sys.stdout.write(color + letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()

def imprimir_mensaje():
# Ejemplo de uso
    mensaje = ("BIENVENIDOS AL MENU PRINCIPAL DE JUEGOS PARA CONTINUAR SELECCIONE UNA DE LAS OPCIONES \n"
               "=======================================\n"
               "J U E G O     D E L    A H O R C A D O\n"
               "=======================================\n"
               "J U E G O     D E L    G A T O\n"
               "=======================================\n"
               "J U E G O     D E L    4  E N   R A Y A\n"
               "=======================================\n"
                "| | | | | | | | | | | | | | | | | | | | | | ")
    animacion_texto(mensaje, 0.01, Fore.YELLOW)
