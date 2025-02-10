'''
Nombre del equipo: Algoritmos anarquistas
Integrantes: Héctor Jésus Méndez Santiago, Jésus Alberto Ramírez Salinas y Addi Toro Chávez.
Fecha: 2 de febrero de 2025.
Descripción: Módulo principal de juegos.
'''
from gato_ordinario import menu_principal_gatos
from ahorcado_ordinario import menu_principal_ahorcado
from rayas_ordinario import  menu_principal_4rayas
from batalla_naval_ordinario import  menu_princial_batalla_naval
from caballos_ordinario import menu_principal_caballos
from texto_ordinario import imprimir_mensaje

def menu_principal_juegos():
        """
        Muestra el menú de opciones del programa
        :return: La función devuleve la selección del usuario,dentro del menú de opciones
        """
        print("Opciones de juego: ")
        print("1) Juego del ahorcado")
        print("2) Juego del Gato")
        print("3) Juego de 4 en rayas")
        print("4) Batalla naval")
        print("5) Carrera de caballos")
        print("0) Salir")
        opcion = (input("Teclea la opción que desea realizar: "))
        while not opcion.isnumeric():
            print("opción no válida")
            opcion = input("Ingrese número nuevamente: ")
        opcion = int(opcion)
        return opcion


if __name__ == '__main__':
    salir=1
    while salir != 0:
        print()
        imprimir_mensaje()
        opciones = menu_principal_juegos()
        if opciones == 1:
              menu_principal_ahorcado()
        elif opciones == 2:
                menu_principal_gatos()
        elif opciones == 3:
                menu_principal_4rayas()
        elif opciones == 4:
                menu_princial_batalla_naval()
        elif opciones == 5:
                menu_principal_caballos()
        elif opciones == 0:
            salir = 0
            print("Salió del programa.")
            break
        else:
            print("opcion incorrecta")