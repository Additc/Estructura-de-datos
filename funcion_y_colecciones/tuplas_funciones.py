"""
Nombre: Addi Toro Chavez
Fecha: 19 de noviembre del 2024
Descripción:
Tuplas en funciones
"""
def calificacion(calificaciones):
    promedio_parcial=sum(calificaciones[0:3])/3
    promedio_final= (promedio_parcial+calificaciones[3])/2
    return promedio_parcial,promedio_final


print("Calificaciones del parcial ")

primer_parcial=float(input("Ingrese calificación del primer parcial: "))
segundo_parcial=float(input("Ingrese calificación del segundo parcial: "))
tercer_parcial=float(input("Ingrese calificación del tercer parcial: "))
ordinario=float(input("Ingrese calificación del ordinario parcial: "))
calificaciones=(primer_parcial,segundo_parcial,tercer_parcial,ordinario)

tupla_final=calificacion(calificaciones)
print(f"Su calificación del parcial es: {tupla_final[0]} y su calificación final es: {tupla_final[1]} ")

