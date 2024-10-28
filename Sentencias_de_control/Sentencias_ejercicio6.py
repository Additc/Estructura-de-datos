'''
Nombre: Addi Toro Chávez
Fecha: 23 de Octubre de 2024
Descripción:
Ejercicio 6 de sentencia en python.

Este programa mostrará los detalles del tour turístico Ecoturixtlán de acuerdo a las siguientes tarifas:

    Precio de un adulto: $ 200.00
    Precio de un niño: $ 100.00

Además, si la visita son los lunes, martes y jueves, se tiene un descuento del 10 %.

Para ello:
a) Solicite al usuario el nombre de la persona a cargo.
b) Defina con valores constantes el precio del boleto del adulto y del niño.
c) Solicite el número de adultos y de niños.
d) Pregunte el día de la semana.
e) Calcule el costo total.
f) Muestre los detalles del cliente y el día, así como el costo total.
'''

print("*** Tour turístico Ecoturixtlán ***")
persona_encargada=input("Ingrese su nombre: ")
niño=int(input("Ingrese el número de niños: "))
adultos=int(input("Ingrese el número de adultos: "))
dia_semana=input("Ingrese dia de la semana: ")
print()
adultos_total= 200*adultos
niños_total = 100* niño
total = adultos_total + niños_total

if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "jueves":
     print("Tiene un descuento del 10%")
     print(f"Gracias por tu visita {persona_encargada} en este día {dia_semana}")
     print(f"El costo total es de ${(total) - (((total) * 10) / 100)}")
else:
    print(f"Gracias por tu visita {persona_encargada} en este día {dia_semana}.")
    print(f"El costo total es de ${total}.")