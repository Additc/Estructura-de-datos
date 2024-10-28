'''
Nombre: Addi Toro Chávez
Fecha: 23 de Octubre de 2024
Descripción:
Ejercicio 5 de sentencia en python.

a) Solicite al usuario sus tres calificaciones parciales y la calificación del ordinario.
b) Calcule el promedio y determine si aprobó (calificación mínima de 6.0).
d) Muestre el promedio (utilizando un decimal) y el mensaje: "¡Felicidades! Aprobaste.", o el mensaje: "Lo siento, no aprobaste.", según sea el caso.
'''
parcial_1=float(input("Ingrese calificación del primer parcial: "))
parcial_2=float(input("Ingrese calificación del segundo parcial: "))
parcial_3=float(input("Ingrese calificación del tercer parcial: "))
ordinario=float(input("Ingrese calificación del ordinario: "))

calificacion = float((parcial_1/6) + (parcial_2/6) + (parcial_3/6))
calificacion = float((calificacion + ordinario/2))
if calificacion >= 6.0:
    print(f"Tu calificacion final es de {(calificacion):.1f} : ¡Felicidades! Aprobaste ")
else:
    print("Lo siento, no aprobaste :(")