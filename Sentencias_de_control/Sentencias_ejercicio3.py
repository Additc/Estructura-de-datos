'''
Nombre: Addi Toro Chávez
Fecha: 23 de Octubre de 2024
Descripción:
Ejercicio 3 de sentencias en python.

Este programa determinará un descuento en compras en "La cona", de acuerdo a lo siguiente:

    Si tiene membresía, obtiene un 5 % de descuento en todas sus compras.
    Si tiene la membresía y su compra fue mayor o igual a $ 1000.00, entonces el descuento es del 8 %.
    Si no tiene la membresía, no obtiene ningún descuento y se invita a ser miembro.

Para ello:

a) Solicite al usuario la cantidad comprada en la tienda.
b) Pregunte al usuario si cuenta con la membresía (Si/No).
c) Utilice la lógica adecuada para determinar el total a pagar.
d) Muestre el descuento y el total a pagar en consola utilizando dos decimales.
'''

compra=float(input("Ingrese la cantidad de compra: "))
membresia=input("¿Cuenta con la membresia?: ")


if compra >= 1000.00 and membresia == "si":
    print("Tiene un descuento  del 8%")
    print(f"EL total de su compra es de: {(compra - (compra * 8)/100):.2f}")
elif membresia == "si":
    print("Tiene un descuento del 5%")
    print(f"El total de su compra es de: {(compra - (compra * 5)/100):.2f}")
else:
    print("Se le invita a ser miembro de la tienda para obtener un descuente de hasta el 8%.")