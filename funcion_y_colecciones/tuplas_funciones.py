"""
Nombre: Addi Toro Chavez
Fecha: 19 de noviembre del 2024
Descripción:
Tuplas en funciones
"""

print("Calificaciones del parcial ")

primer_parcial=float(input("Ingrese calificación del primer parcial: "))
segundo_parcial=float(input("Ingrese calificación del segundo parcial: "))
tercer_parcial=float(input("Ingrese calificación del tercer parcial: "))
ordinario=float(input("Ingrese calificación del ordinario parcial: "))

calificaciones=(primer_parcial,segundo_parcial,tercer_parcial,ordinario)
p1,p2=(calificacion)
print(f"Su calificación del parcial es: {p1} y su calificación final es: {p2} ")

def calificacion(calificaciones):
    promedio_parcial=sum(calificaciones[0:2]/3)
    promedio_final= (promedio_parcial+calificaciones[3])/2
    tupla_promedios=(promedio_parcial,promedio_final)
    return  tupla_promedios

