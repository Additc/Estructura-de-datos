"""
Nombre: Addi Toro Chavez
Fecha: 7 de diciembre del 2024
Descripción:
Ejercicio 2  exámen, conversiones de números
"""


#Definición del menú de conversiones
def menu():
    print()
    print("Conversion entre las bases decimal, binario y hexadecimal")
    print("Ingrese una de las opciones: ")
    print("1._Convertir de decimal a binario y hexadecimal.")
    print("2._Convertir de binario a decimal y hexadecimal.")
    print("3._Convertir de hexadecimal a decimal y binario.")
#Se obtiene la opción del usuario
    opcion=int(input("Ingrese una opción: "))
    return opcion

#Definción de la primera opción, convirtiendo un número decimal a binario y este a hexadecimal.
def deci_bina_hexa():
#El usuario ingresa un número de base decimal.
    numero_decimal=int(input("Ingrese número en base decimal: "))
    entero=numero_decimal
    d=[]
#Se realiza la implementación de la lógica para convertir el número decimal a binario.
    print(f"El número decimal {numero_decimal}", end=" ")
    while(numero_decimal>=1):
        d.append(numero_decimal%2)
        numero_decimal= numero_decimal//2
    s=d[::-1]
#Se muestra en pantalla el número en binario.
    print("es  en binario", end = " ")
    for k in s:
        print(k,end = " ")
#Se implementa la lógica para convertir el número decimal a hexadecimal.
    hexa = " "
#Defino una varible que almacena una cade de representación de los número decimales a hexadecimal.
    hexadecimal = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "10"
    while (entero >= 1):
        residuo = (entero % 16)
        hexa = hexadecimal[residuo] + hexa
        entero //= 16
#Se muestra en pantalla el número decimal convertido a hexadecimal.
    print(f" y {hexa} en hexadecimal", end=" ")
    print()



#Definición de la segunda opción, convirtiendo un número binario a decimal y este a hexadecimal.
def bina_deci_hexa ():
#Se declarán un contadores.
    s = 0
    i = 0
#Se solicita un número en base binario.
    numero_binario=int(input("Ingrese número en base binario: "))
#Se implementa la lógica necesaria para convertir el número binario a decimal.
    print(f"El número binario {numero_binario}", end=" ")
    while (numero_binario>=1):
        d=numero_binario%10
        numero_binario=numero_binario//10
        s=s+d*pow(2,i) # Hasta este punto (s) tiene el numero en base decimal
        i+=1
#Se muestra en pantalla la conversión del número binario a decimal
    print(f"es {s} en decimal", end=" ")

#Implementación de lógica para la conversión a número hexadecimal.
    hexa=" "
#Defino una varible que almacena una cade de representación de los número decimales a hexadecimal.
    hexadecimal="0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"
    entero=s
    while(entero>=1):
        residuo=(entero%16)
        hexa = hexadecimal[residuo]+hexa
        entero//=16
#Se muestra el pantalla la conversión del número decimal a hexadecimal
    print(f" y {hexa} en hexadecimal",end=" ")
    print()

#Definición de la segunda opción, convirtiendo un número hexadecimal a decimal y este a binario.
def hexa_deci_bina():
    hexadecimal ={'0':0,'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
#Se solicita al usuario el número de base hexadecimal.
    numero_hexadecimal=input("Ingrese número en base hexadecimal: ")
#Obtenemos la longitud del número, para iterar en ella.
    l=len(numero_hexadecimal)
    numero_decimal=0
#Se implementa la lógica dentro del for para convertirlo a número decimal.
    for i in range(l):
        digito=numero_hexadecimal[i]
        valor=hexadecimal[digito]
        elevacion= l -1-i
        numero_decimal += valor*(16** elevacion)
#Se muestra en pantalla la conversión a número decimal
    print(F"El número hexadecimal {numero_hexadecimal} es  {numero_decimal} en decimal",end=" ")

#Implemetación para convertir número decimal a número binario.
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

#Establezco mis ciclo que estará repitiendose de acuerdo a la opción del usuario.
#Dentro de ella establezco mis condiciones según sea la opcion seleccionada y llamo a la función correspondiente
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