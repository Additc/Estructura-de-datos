'''
Nombre: Addi Toro Chavez
Fecha: 8 de enero de 2025.
Descripción: Saludar main
'''
def menu():
    print("Selecciones la operación que desea realiza: ")
    print("1) Sumar ")
    print("2) Restar ")
    print("0) Salir")
    opcion=input("Teclea la opción que desea realizar: ")
    while not opcion.isnumeric():
        print("opción no válida")
        opcion= input("ingrese número nuevamente: ")
    opcion=int(opcion)
    return opcion


def suma (numero1,numero2)->float:
    total_suma= numero1+numero2
    return total_suma


def resta(numero1,numero2)->float:
    total_resta= numero1-numero2
    return total_resta



if __name__ == '__main__':
    op=1
    while op!=0:
        opcion=menu()
        if opcion==1:
            num1 = input("Ingrese primer número a sumar: ")
            while not num1.isnumeric():
                print("opción no válida")
                num1= input("ingrese nuevamente el número a sumar: ")
            num1 = float(num1)

            num2= input("Ingrese segundo número a sumar: ")
            while not num2.isnumeric():
                print("opción no válida")
                num2 = input("ingrese nuevamente el número a sumar: ")
            num2 = float(num2)
            total=suma(num1,num2)
            print(f"El total de la suma del número {num1} y el número {num2} es {total}")
            print()
        elif opcion==2:
            num1 = input("Ingrese primer número a restar: ")
            while not num1.isnumeric():
                print("opción no válida")
                num1= input("ingrese nuevamente el número a restar: ")
            num1 = float(num1)

            num2= input("Ingrese segundo número a restar: ")
            while not num2.isnumeric():
                print("opción no válida")
                num2 = input("ingrese número nuevamente el número a restar: ")
            num2 = float(num2)
            total=resta(num1,num2)
        elif opcion == 0:
            opcion = 0
            print("Salió del programa")
        else:
            print("opcion incorrecta")