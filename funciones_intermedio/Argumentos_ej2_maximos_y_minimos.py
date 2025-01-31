'''
Nombre: Addi Toro Chavez
Fecha: 28 de enero de 2025.
Descripción: Argumenos ejercicio 2 máximos y mínimos.
'''

def menu ():
    """
    Función que muestra el menú de opciones de la calculadora.
    :return: Regresa de la opción seleccionada por el usuario.
    """
    print()
    print("1) Encontrar máximo y mínimo de numeros")
    print("0) salir")
    opcion=(input("Teclea la opción que desea realizar: "))
    while not opcion.isnumeric():
        print("opción no válida")
        opcion= input("Ingrese una opción nuevamente: ")
    opcion=int(opcion)
    return opcion

def cadena_a_flotante (cadena):
    """
    Función que convierte una cadena a un número flotante.
    :param cadena: Cadena ingresada por el usuario.
    :return:  Regresa el número flotante si cumple con el formato, en caso contrario, devuelve None.
    """
    no_puntos=cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".","")
    if revisar_cadena.isnumeric() and no_puntos in (0,1) and no_guiones in (0,1):
        return float(cadena)
    else:
        return None


def ingresar_numeros()->None:
    """
    Función donde el usuario ingresa los números.
    :return: La función no regresa nada.
    """
    numeros=[]
    num_cadena = input(f"Ingresa la calificación [{len(numeros) + 1}] o presiona enter para continuar: ")

    while bool(num_cadena):
        numero = cadena_a_flotante(cadena= num_cadena)
        if numero is None:
            print("Formato no válido, intenta nuevamente.")
        else:
            numeros.append(numero)

        num_cadena = input(f"Ingresa la calificación [{len(numeros) + 1}] o presiona enter para continuar: ")
    calcular_maximo_minimo( *numeros)

def calcular_maximo_minimo(*vargs):
    """
    Función que calcula el mínimo y el máximo de los número ingresados por el usuario.
    :param vargs: Números ingresados por el usuario.
    :return:
    """

    if len(vargs) != 0:
        print(f"El numero mínimo es: {min(vargs)}")
        print(f"El numero máximo es: {max(vargs)}")

def main() -> None:
    """
    Función principal.
    :return:
    """
    opcion = None
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            ingresar_numeros()
            calcular_maximo_minimo()
        elif opcion == 0:
            opcion = 0
            print("Salió del programa")
            break
        else:
            print("opción incorrecta")


if __name__ == '__main__':
     main()