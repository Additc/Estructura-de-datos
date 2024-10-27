'''
Addi Toro Chavez
16 de octubre de 2024.
Descripción:
Ejercicio de operadores relacionales en python
'''
numero1,numero2=float(input("ingresa numero1: ")),float(input("ingresa numero2: ")) # ingresamos 2 números de tipo flotante

#Existen varios operadores relaciones, en este programa se mostrara la funcion de los siguientes:
#(< y >) Menor y mayor que.
# (<= y>=) Menor igual y mayor igual que.
# (==) Igual igual que.
# (!=) Diferente que.

# Muestra en pantalla si es verdadero o falso las siguientes comparaciones.
print(f"¿El numero {(numero1):.2f} es mayor que {(numero2):.2f} ?{numero1>numero2}") # Comparación, si el primer número es mayor que el segundo número.
print(f"¿El numero {(numero1):.2f} es mayor o igual que {(numero2):.2f} ?{numero1>=numero2}") # Comparación, si el primer número es mayor o igual que el segundo número.
print(f"¿El numero {(numero1):.2f} es igual al numero {(numero2):.2f} ?{numero1==numero2}") # Comparación, si el primer número es igual igual que el segundo número.
print(f"¿El numero {(numero1):.2f} es menor que {(numero2):.2f} ?{numero1<numero2}") # Comparación, si el primer número es menor que el segundo número.
print(f"¿El numero {(numero1):.2f} es menor o igual que {(numero2):.2f}?{numero1<=numero2}") # Comparación, si el primer número es menor o igual que el segundo número.
print(f"¿El numero {(numero1):.2f} es diferente que {(numero2):.2f} ?{numero1!=numero2}") # Comparación, si el primer número es diferente que el segundo número.