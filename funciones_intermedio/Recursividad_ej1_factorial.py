'''
Nombre: Addi Toro Chavez
Fecha: 28 de enero de 2025.
Descripción: Recursividad ejercicio 1 factorial de un número.
'''

def menu():
    """
        Función que muestra el menú de opciones de la calculadora.
        :return: retorna de la opción seleccionada por el usuario.
        """
    print()
    print("1) Calcular el factorial de un número")
    print("0) salir")
    opcion = (input("Teclea la opción que desea realizar: "))
    while not opcion.isnumeric():
        print("opción no válida")
        opcion = input("Ingrese una opción nuevamente: ")
    opcion = int(opcion)
    return opcion


def factorial(numero):
    """
    Función que calcula el factorial de un número.
    :param numero: Número ingresado por el usuario.
    :return: Factorial del número ingresado por el usuario.
    """
    if numero==0:
        return 1
    else:
        return numero*factorial(numero-1)


def es_numero_valido(cadena: str) -> bool:
    """
    Función que determina si el número ingresado se encuentra entre 0 y un entero positivo.
    :param cadena: Cadena a validar.
    :return: Si la cadena cumple con el formato
    """
    if cadena.isnumeric():
        return True

    else:
        return False


def main() -> None:
    """
    Función principal.
    :return:
    """
    opcion = None
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            num_cadena = input("Ingresa un número entre 0 y un entero positivo: ")
            if es_numero_valido(num_cadena):
                numero = int(num_cadena)
                factorial(numero)
                print(f"el factorial del numero dado es: {factorial(numero)}")
                print("Fin del programa")
                break
        elif opcion == 0:
            opcion = 0
            print("Salió del programa")
            break
        else:
            print("opción incorrecta")


if __name__ == '__main__':
     main()