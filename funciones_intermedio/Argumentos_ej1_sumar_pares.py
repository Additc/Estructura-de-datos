'''
Nombre: Addi Toro Chavez
Fecha: 28 de enero de 2025.
Descripción: Argumenos ejercicio 1 suma de numeros pares
'''

def menu ():
    """
    Función que muestra el menú de opciones de la calculadora.
    :return: Regresa de la opción seleccionada por el usuario.
    """
    print()
    print("Calculadora")
    print("1) sumar todos lo números ingresados")
    print("0) salir")
    opcion=(input("Teclea la opción que desea realizar: "))
    while not opcion.isnumeric():
        print("opción no válida")
        opcion= input("Ingrese una opción nuevamente: ")
    opcion=int(opcion)
    return opcion

def cadena_a_entero (cadena:str)->int|None:
    """
    Función que convierte la cadena a número entero.
    :param cadena: Cadena a convertir.
    :return: Regresa el número entero si cumple con el formato, en caso contrario, devuelve None.
    """
    no_guiones=cadena.count("-")
    revisar_cadena=cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0,1):
        return int(cadena)
    else:
        return None


def ingresar_numeros()->None:
    """
    Función donde el usuario ingresa los números a sumar.
    :return: La función no regresa nada.
    """
    numeros=[]
    num_cadena = input(f"Ingresa la calificación [{len(numeros) + 1}] o presiona enter para continuar: ")

    while bool(num_cadena):
        numero = cadena_a_entero(cadena= num_cadena)
        if numero is None:
            print("Formato no válido, intenta nuevamente.")
        else:
            numeros.append(numero)

        num_cadena = input(f"Ingresa la calificación [{len(numeros) + 1}] o presiona enter para continuar: ")
    calcular_suma( *numeros)

def calcular_suma(*vargs):
    """
    Función que calcula la suma de los números pares ingresados por el usuario.
    :param vargs: Números ingresados por el usuario.
    :return:La suma de los número pares.
    """
    suma = 0
    if len(vargs) != 0:
        for numero in vargs:
            if numero%2 == 0:
                suma +=numero
        print(f"La suma de todos los números pares es: {suma}")

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
            calcular_suma()
        elif opcion == 0:
            opcion = 0
            print("Salió del programa")
            break
        else:
            print("opción incorrecta")


if __name__ == '__main__':
     main()