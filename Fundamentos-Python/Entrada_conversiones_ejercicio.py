'''
Nombre: Addi Toro Chavez
Fecha: 19 de octubre del 2024
Descripción:
Conversión de cadenas a int, float y boolean mediante la interacción con consola.

 Escribe un programa de nombre Entrada_conversiones_ejercicio.py que realice lo siguiente:

a) Pida los datos de los profesores utilizando nombres de variables adecuadas, la función input y el casting:

        Nombre (cadena).
        No. de cubículo (int).
        Horas de que imparte clase a la semana (float con 3 decimales).
        ¿Tiene más de 5 años en la unsij? (booleno).

b) Muestre los datos en consola de forma adecuada.

Nota: Asuma que el usuario siempre va a ingresar números cuando se requiera.
'''
nombre=input(print("ingrese nombre del profesor: ")) # Ingresamos el nombre del docente.
No_cubiculo= int(input(print("ingrese número de cubículo del profesor: "))) # Ingresamos el numero del cubículo.
horas_por_semana= float(input(print("ingrese número de horas impartidas porr semana"))) # Ingresamos las horas por semana que son impartidas por el docente.

Años_en_la_unsij = input("¿Tiene más de 5 años en la UNSIJ?: ")
Años_en_la_unsij = Años_en_la_unsij.lower() == "si" #Transformamos la cadena a minúsculas para haacer la comparación.
print()
# Se muestra en pantalla los datos registrados
print(f"Nombre: {nombre}")
print(f"Número de cubículo: {No_cubiculo}")
print(f"Horas que imparte clase a la semana: {(horas_por_semana):.3f}")
print(f"¿Tiene más de 5 años en la UNSIJ?: {Años_en_la_unsij}")