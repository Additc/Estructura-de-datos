"""
Nombre: Addi Toro Chavez
Fecha: 7 de diciembre del 2024
Descripción:
Ejercicio 2  exámen, conversiones de números
"""



def menu():
    print()
    print("Conversion entre las bases decimal, binario y hexadecimal")
    print("Ingrese una de las opciones: ")
    print("1._Convertir de decimal a binario y hexadecimal.")
    print("2._Convertir de binario a decimal y hexadecimal.")
    print("3._Convertir de hexadecimal a decimal y binario.")
    opcion=int(input("Ingrese una opción: "))
    return opcion

def deci_bina_hexa():
    numero_decimal=int(input("Ingrese número en base decimal: "))
    entero=numero_decimal
    d=[]
    print(f"El número decimal {numero_decimal}", end=" ")
    while(numero_decimal>=1):
        d.append(numero_decimal%2)
        numero_decimal= numero_decimal//2
    s=d[::-1]
    print("es  en binario", end = " ")
    for k in s:
        print(k,end = " ")

    hexa = " "
    hexadecimal = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "10"
    while (entero >= 1):
        residuo = (entero % 16)
        hexa = hexadecimal[residuo] + hexa
        entero //= 16
    print(f" y {hexa} en hexadecimal", end=" ")
    print()



def bina_deci_hexa ():
    s = 0
    i = 0
    numero_binario=int(input("Ingrese número en base binario: "))
    print(f"El número binario {numero_binario}", end=" ")
    while (numero_binario>=1):
        d=numero_binario%10
        numero_binario=numero_binario//10
        s=s+d*pow(2,i) # Hasta este punto (s) tiene el numero en base decimal
        i+=1
    print(f"es {s} en decimal", end=" ")
    hexa=" "
    hexadecimal="0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"
    entero=s
    while(entero>=1):
        residuo=(entero%16)
        hexa = hexadecimal[residuo]+hexa
        entero//=16
    print(f" y {hexa} en hexadecimal",end=" ")
    print()

def hexa_deci_bina():
    hexadecimal ={'0':0,'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    numero_hexadecimal=input("Ingrese número en base hexadecimal: ")
    l=len(numero_hexadecimal)
    numero_decimal=0
    for i in range(l):
        digito=numero_hexadecimal[i]
        valor=hexadecimal[digito]
        elevacion= l -1-i
        numero_decimal += valor*(16** elevacion)
    print(F"El número hexadecimal {numero_hexadecimal} es  {numero_decimal} en decimal",end=" ")

    entero = numero_decimal
    d = []
    while (numero_decimal >= 1):
        d.append(numero_decimal % 2)
        numero_decimal = numero_decimal // 2
    s = d[::-1]
    print("Y  en binario", end=" ")
    for k in s:
        print(k, end=" ")
    print()

op = 1
while op != 0:
    opcion = menu()
    if opcion == 1:
        deci_bina_hexa()
    elif opcion == 2:
        bina_deci_hexa()
    elif opcion == 3:
        hexa_deci_bina()
    elif opcion == 0:
        op = 0
        print("Salió del programa")
    else:
        print("opción incorrecta")