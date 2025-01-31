'''
Nombre: Addi Toro Chavez
Fecha: 28 de enero de 2025.
Descripción: Recursividad ejercicio 2 potenciación de números.
'''



def menu():
    """
        Función que muestra el menú de opciones de la calculadora.
        :return: retorna de la opción seleccionada por el usuario.
        """
    print()
    print("1) Calcular laa potenciación de 2 números")
    print("0) salir")
    opcion = (input("Teclea la opción que desea realizar: "))
    while not opcion.isnumeric():
        print("opción no válida")
        opcion = input("Ingrese una opción nuevamente: ")
    opcion = int(opcion)
    return opcion

def es_numero_valido(cadena: str,cadena_2:str) -> bool:
    """
    Función que determina si el número ingresado se encuentra entre 0 y un entero positivo.
    :param cadena: Cadena a validar.
    :return: Si la cadena cumple con el formato
    """
    if cadena.isnumeric() and cadena_2.isnumeric():
        return True

    else:
        print("Formato no válido")
        print("Fin del programa")
        return False

def elevacion(numero_a,numero_b):
    """
    Función que realiza la llamada recursiva para obtener la exponenciación de los
    números ingresados.
    :param numero_a: Número base ingresado por el usuario.
    :param numero_b: Número exponente ingresado por el usuario.
    :return: Total de la exponenciación.
    """
    if numero_b==0:
        return 1
    else:
        total = numero_a*elevacion(numero_a,numero_b-1)
        return total


def main() -> None:
    """
    Función principal, donde el usuario ingresa el número base y el exponente.
    :return: El resultado de la exponenciación o en dado caso este sea 0 indeterminado.
    """
    opcion = None
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            num_cadena = input("Ingresa la base a, un número entre 0 y un entero positivo: ")
            num_cadena2 = input("Ingresa el exponente b, un número entre 0 y un entero positivo: ")
            if es_numero_valido(num_cadena,num_cadena2):
                numero_a = int(num_cadena)
                numero_b = int(num_cadena2)
                if numero_a ==0 and numero_b==0:
                    print(f"{numero_a}^{numero_b} es: Indeterminado")
                    break
                else:
                    total=elevacion(numero_a,numero_b)
                    if total==0:
                        print("Indeterminado")
                    else:
                        print(f"{num_cadena}^{num_cadena2} es: {elevacion(numero_a,numero_b)}")
                        print("Fin del programa")
                        break
            else:
                break
        elif opcion == 0:
            opcion = 0
            print("Salió del programa")
            break
        else:
            print("opción incorrecta")


if __name__ == '__main__':
     main()
