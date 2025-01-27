'''
Nombre: Addi Toro Chavez
Fecha: 8 de enero de 2025.
Descripción: Saludar main
'''
from Juego_gato import tiros
from Juego_ahorcado import jugar_ahorcado
from texto import imprimir_mensaje

def menu_principal():
        """
        Muestra el menú de opciones del programa
        :return: La función devuleve la selección del usuario,dentro del menú de opciones
        """
        print("Opciones de juego: ")
        print("1) Juego del ahorcado")
        print("2) Juego del Gato")
        print("3) Juego de 4 en rayas")
        print("0) Salir")
        opcion = (input("Teclea la opción que desea realizar: "))
        while not opcion.isnumeric():
            print("opción no válida")
            opcion = input("Ingrese número nuevamente: ")
        opcion = int(opcion)

        while opcion != 0:
            imprimir_mensaje()
            opcion = menu_principal()
            if opcion == 1:
                jugar_ahorcado()
            elif opcion == 2:
                tiros()
            elif opcion == 3:
                break
            elif opcion == 0:
                opcion = 0
                print("Salió del programa")
                break
            else:
                print("opcion incorrecta")






