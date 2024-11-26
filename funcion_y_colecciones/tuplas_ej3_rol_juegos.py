"""
Nombre: Addi Toro Chavez
Fecha: 16 de noviembre del 2024
Descripción:
Tuplas ejercicio 3 rol de juegos
"""


equipos=[]
contador_equipos=1
equipo= int(input("Ingrese numero de equipos:"))
for i in range (equipo):
    equipo=input("Ingrese nombre del equipo: ")
    equipos.append(equipo)

if len(equipos) == 0:
    print("No hay equipos.")
elif len(equipos) < 2:
    print("Se necesitan mas de 2 equipos.")
else:
    for i in range(len(equipos)):
        for j in range(i + 1, len(equipos)):
            print(f"Partido {contador_equipos}: {equipos[i]} vs {equipos[j]}")
            contador_equipos += 1
print()

"""
Nota: no pude recordar como pidió el código de cierta forma e intente hacerlo a o que entendí.

Declaro mi lista para almacenar los nombre de los equipos, y con ayuda de un ciclo flor almacenos los equipos en la lista.
Con unas condiciones y ciclos de for anidados reaizo el rol de partidos para una jornada.
Se muestra en pantalla los partidos correspondientes.
"""