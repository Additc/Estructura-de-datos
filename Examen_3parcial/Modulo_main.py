'''
Nombre: Addi Toro Chavez
Fecha: 8 de enero de 2025.
Descripción: Saludar main
'''
from gato_alberto import menu_gato,unovscpu,unovsuno
from Juego_ahorcado import menu_ahorcado, jugar_ahorcado
from Juego_4_rayas import menu_4_rayas, jugar_contra_cpu,jugar_contra_jugador
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
        print("4) Juego de carrera de caballos")
        print("5) Juego de batalla naval")
        print("0) Salir")
        opcion = (input("Teclea la opción que desea realizar: "))
        while not opcion.isnumeric():
            print("opción no válida")
            opcion = input("Ingrese número nuevamente: ")
        opcion = int(opcion)
        return opcion


if __name__ == '__main__':
    tablero = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    salir=1
    while salir != 0:
        imprimir_mensaje()
        opciones = menu_principal()
        if opciones == 1:
            while True:
                opcion_ahorcado = menu_ahorcado()
                if opcion_ahorcado == 1:
                    jugar_ahorcado()
                elif opcion_ahorcado == 0:
                    break
                else:
                    print("Opcion no valida. Intentalo nuevamente.")
        elif opciones == 2:
            while True:
                opcion_gato = menu_gato()
                if opcion_gato == 1:
                    unovsuno(tablero)
                elif opcion_gato == 2:
                    unovscpu(tablero)
                elif opcion_gato == 0:
                    break
                else:
                    print("Opcion no valida. Intentalo nuevamente.")
        elif opciones == 3:
            while True:
                opcion_rayas = menu_4_rayas()
                if opcion_rayas == 1:
                    jugar_contra_jugador()
                elif opcion_rayas == 2:
                    jugar_contra_cpu()
                elif opcion_rayas == 0:
                    break
                else:
                    print("Opcion no valida. Intentalo nuevamente.")
        elif opciones == 4:
            while True:
                opcion_gato = menu_gato()
                if opcion_gato == 1:
                    unovsuno(tablero)
                elif opcion_gato == 2:
                    unovscpu(tablero)
                elif opcion_gato == 0:
                    break
                else:
                    print("Opcion no valida. Intentalo nuevamente.")
        elif opciones == 0:
            salir = 0
            print("Salió del programa.")
            break
        else:
            print("opcion incorrecta")






