'''
Nombre del equipo: Algoritmos anarquistas
Integrantes: Héctor Jésus Méndez Santiago, Jésus Alberto Ramírez Salinas y Addi Toro Chávez.
Fecha: 2 de febrero de 2025.
Descripción: Módulo correspondiente al texto de animación en el menú principal.
'''

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
    mensaje=("B I E N V E N I D O S   A L   M E N U   P R I N C I P A L\n"
              "   D E   J U E G O S   P A R A   C O N T I N U A R\n"
              " S E L E C C I O N E   U N A   D E  L A S  O P C I O N E S \n")

    mensaje1 = (
                "===============================================================\n"
                "       || J U E G O     D E L    A H O R C A D O ||     _______     \n"
                "                                                       |/      |    \n"
                "                                                       |      O     \n"
                "                                                       |     /|\    \n"
                "                                                       |      |     \n"
                "                                                       |     / \    \n"
                "                                                      _|___         \n"
                "===============================================================\n")

    mensaje2=(  "===============================================================\n"
                "         || J U E G O     D E L    G A T O ||          /\_/\ \n "
                "                                                     ( o.o ) \n"
                "                                                       > ^ < \n"
                "===============================================================\n")

    mensaje3=(  "===============================================================\n"
                "     || J U E G O     D E L    4  E N   R A Y A  ||  O\n" 
                "                                                       X\n"
                "                                                          O\n"
                "                                                            X \n"
                "===============================================================\n")

    mensaje4=(  "===============================================================\n "
                "   || J U E G O  C A R R E R A  D E  C A B A L L O S || |\ /\  \n "  
                "                                                        \ 0 0  \n "
                "                                                       / \-_-\ \n "
                "                                                      /-----/  \n "
                "===============================================================\n ")

    mensaje5=("=================================================================\n"
                "     || J U E G O   D E   B A T A L L A  N A V A L || |\ \n"
                "                                                      | \ \n"
                "                                                      |  \ \n"
                "                                                   ___|______\n"
                "                                                   \\________/\n"
                "                                            ~~~~~~~~~~~~~~~~~~~~ \n"
                "===============================================================\n")
    mensaje6=("| | | | | | | | | | | | | | | | | | | | | | | | | | | | | ")
    animacion_texto(mensaje,0.001, Fore.RED)
    animacion_texto(mensaje1, 0.001, Fore.LIGHTYELLOW_EX)
    animacion_texto(mensaje2, 0.001, Fore.MAGENTA)
    animacion_texto(mensaje3, 0.001, Fore.BLUE)
    animacion_texto(mensaje4, 0.001, Fore.GREEN)
    animacion_texto(mensaje5, 0.001, Fore.CYAN)
    animacion_texto(mensaje6, 0.001, Fore.WHITE)
