'''
Addi Toro Chavez
27 de octubre de 2024.
Descripción:
Ejercicio 4 de ciclo while en python
Cuenta bancaria
'''
op =1
saldo=0
dinero=0
while op != 0:
    print()
    print(" 0) Salir")
    print(" 1) Consultar dinero")
    print(" 2) Ingresar dinero")
    print(" 3) Retirar dinero")
    op = int(input("Ingrese un número de opción a realizar: "))

    if op == 1:
        print(f"Su saldo actual es de : {saldo}")
    elif op == 2:
        saldo+= float(input("Ingrese la cantidad de dinero: "))
    elif op == 3:
        dinero=float(input("Ingrese cantidad a retirar: "))
        if saldo > dinero:
            saldo = saldo-dinero
            print(f"Usted ha retirado: {dinero}")
        else:
            print("Acción incorrecta")
    elif op == 0:
         op=0
         print("Salio de la cuenta")
    else:
        print("opción incorrecta")

"""
Declaro 2 contadores, uno que acumulará y me ayudará a saber el total de mi saldo, y otro que me ayudará a saber la cantidad que
 el usuario desea retirar.
 Establezco mi condición while, hasta que sea difrente de cero este me mostrará el menú de opciones establecido.
 Establezco la condiciones que se aplicarán de acuerdo a la opción seleccionada por el usuario.
 De acuerdo a la opción seleccionada, se mostrará en pantalla el saldo, el dinero retirado, o alguna opción incorrecta.
"""