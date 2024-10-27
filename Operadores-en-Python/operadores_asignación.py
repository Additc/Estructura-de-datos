'''
Addi Toro Chavez
15 de octubre de 2024.
Descripción:
Ejercicio de operadores de asignación en python
'''
# Ejemplo de asignación múltiple
num1,num2=5,10 # Asignación de los valores.
num3,num4=9.14,"chay" # Asignación de un valor fotante y una cadena.
print(num1,num2,num3,num4) # Se muestra en pantalla los datos

# Se crean nuevas variables para una asignación múltiple
num5,num6 = num1+num2,num1-num2 # La variable núm5 guardará la suma de los 2 primeros valores.
                                # Y la vaiable num6 guardará la resta de los 2 valores.
# Se muestra en pantalla los resultados.
print(num5,num6)

#Ejemplo de  asignación concatenada
num7=num8=num9=10
print(num7) # Se muestra en pantalla el valor asigando a través de la concatenación.

#Intercambio de variables
num10,num11 ="alberto","geto" # La variable num10= alberto y la variable num11=geto.
print(num10,num11)# Se muestra en pantalla.
num11,num10=num10,num11 # Se realiza el intercambio de variables.
# Ahora la variable num11=alberto y la variable num10=geto.
print(num10,num11)  # Se muestra en pantalla.

nombre,apellido=input("ingresa nombre: "),input("ingresa apellido: ") # Una de las posibles manera de ingresar datos.
