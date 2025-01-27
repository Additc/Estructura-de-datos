
def menu ():
    """
    Función que muestra el menú de opciones de la calculadora.
    :return: retorna de la opción seleccionada por el usuario.
    """
    print()
    print("Calculadora")
    print("1) sumar todos lo numeros ingresados")
    print("2) Multiplicar todos los numeros ingresados")
    print("0) salir")
    opcion=(input("Teclea la opción que desea realizar: "))
    while not opcion.isnumeric():
        print("opción no válida")
        opcion= input("Ingrese una opción nuevamente: ")
    opcion=int(opcion)
    return opcion

def sumar(*vargs)->float:
    resultado=0
    for i in vargs:
        resultado+=i

    return resultado # otra manera seria return sum(vargs)

def multiplicar(*vargs)->float:
    resultado=1
    for i in vargs:
        resultado *=i
    return resultado



def cadena_a_flotante (cadena):
    """
    Función que convierte una cadena a un flotante
    :param cadena: Cadena introducida por el usuario
    :return: Número flotante
    """
    no_puntos=cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".","")
    if revisar_cadena.isnumeric() and no_puntos in (0,1) and no_guiones in (0,1):
        return float(cadena)
    else:
        return None
op=1
while op!=0:
    opcion = menu()
    if opcion==1:
        numero1 =input("Ingrese primer número a sumar: ")
        numero_suma1=cadena_a_flotante(numero1)
        while numero_suma1 is None:
            numero1= input("Acción inválida, ingrese nuevamente el primer número a sumar: ")
            numero_suma1 = cadena_a_flotante(numero1)


        numero2 =input("Ingrese segundo número a sumar: ")
        numero_suma2=cadena_a_flotante(numero2)
        while numero_suma2 is None:
            numero2= input("Acción inválida, ingrese nuevamente el segundo número a sumar: ")
            numero_suma2 = cadena_a_flotante(numero2)

        total=sumar(numero_suma1,numero_suma2)
        print(f"El total de la suma es: {total}")

    elif opcion ==2:
        numero1 = input("Ingrese primer número a multiplicar: ")
        numero_multiplicar1 = cadena_a_flotante(numero1)
        while numero_multiplicar1 is None:
            numero1 = input("Acción inválida, ingrese nuevamente el primer número a multiplicar: ")
            numero_multiplicar1 = cadena_a_flotante(numero1)

        numero2 = input("Ingrese segundo número a multiplicar: ")
        numero_multiplicar2 = cadena_a_flotante(numero1)
        while numero_multiplicar2 is None:
            numero2 = input("Acción invalida, ingrese nuevamente el segundo núumero a multiplicar: ")
            numero_multiplicar2 = cadena_a_flotante(numero2)

        total=multiplicar(numero_multiplicar1,numero_multiplicar2)
        print(f"El total de la multiplicación es: {total}")

    elif opcion == 0:
        opcion = 0
        print("Salió del programa")
        break
    else:
        print("opción incorrecta")