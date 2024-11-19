"""
Nombre: Addi Toro Chavez
Fecha: 19 de noviembre del 2024
Descripción:
Tuplas en puthon
"""
"""
Una lista es ordenada, inmutable, y los elementos se encierran en corchetes.
Las tuplas son inmultables, para las tuplas ocupamos parenteseis. 
"""
print("**Ejemplo de tupla**")
fechas_cumpleaños=("12-19","12-27","01-10","10-18","11-01","09-30","08-25","01-06","10-21","04_11","03-06","08-02")
print(fechas_cumpleaños)

for fecha in fechas_cumpleaños:
    print(f"feliz cumpleaños al:{fecha}", end= " ")

print()

print("Serie de leibniz")
pi_serie=(4,-4/3,4/5,-4/7,4/9,-4/11,4/13,-4/15,4/17,-4/19)
print(sum(pi_serie[0:2]))# 3 elementos
print(sum(pi_serie[0:4]))# 5 elementos
print(sum(pi_serie[0:7]))# 8 elementos
print(sum(pi_serie[0:9]))# 10 elementos
print()

print("**Ejemplos con coordenadas**")
punto1=(1,0)
punto2=(5,3)
print(f"coordenadas en tuplas: {punto1} y {punto2}")

#desempaquetado de tuplas
x1,y1=punto1
x2,y2=punto2

delta=(y2-y1)/(x2-x1)
b=y1-delta*x1

print(f"La exprresion de la recta es y= {delta}x {b}")