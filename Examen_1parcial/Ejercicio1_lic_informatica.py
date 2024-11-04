'''
Nombre: Addi Toro Chavez
Fecha: 27 de octubre de 2024.
Descripción:
Este programa imprime en consola los números, separados por comas, del 1 hasta un número ingresado por el usuario.

Sin embargo, se deben sustituir los siguientes valores:

    3 o sus múltiplos por la palabra "Licenciatura".
    5 y sus múltiplos por la palabra "Informática".
    Múltiplos de 3 y 5 por la frase "Licenciatura en Informática" y se imprima un salto de línea en lugar de la coma.

Para ello:
a) Solicite un número en consola.
b) Realizar la lógica adecuada para imprimir los números o mensajes adecuados.
c) Mostrar los resultados en consola.
'''

numero_final=int(input("ingrese número final: ")) # Ingresamos el número final al cual llegará nuestra serie de números.
contador = 1 # Inicializamos el contador en 1.
while contador <= numero_final: # Establecemos la condición, mientras que el contador se menor o igual al número final.

        if contador % 3 == 0 and contador % 5 == 0: # Establecemos la primer condición que indicará si ambos son múltiplos de 5 y 3.
            print("licenciatura en informática",end = ", ") # Se cumple el caso y mostramos en pantalla licenciatura en informática.
            print()
        elif contador % 3 == 0: # Establecemos otra condición que indicará cuales son los múltiplos de 3.
            print("licenciatura",end = ", ") # Si son múltiplos se mostrará en pantalla la palabra licenciatura.
        elif contador % 5 == 0:# Condición que indicará cuales son los múltiplos de 5.
            print("informática",end=", ")# Si se cumple el caso se mostrará en pantalla informática
        else:
         print(contador,end=", ")# Si ninguna de las condiciones se cumple se muestra el contador en pantalla o el número.
        contador += 1 # Aumentamos contador

