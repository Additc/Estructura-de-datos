'''
Nombre: Addi Toro Chávez
Fecha: 28 de Octubre de 2024
Descripción:
Ciclo while en python
'''

# Crear una lista vacía
alumnos =[ ]
alumnos.append("Hector")
alumnos.append("Addi")
alumnos.append("Alberto")
alumnos.append("Addi")
print(alumnos)
print(alumnos[1])

#para insertar valores en un índice específico
alumnos.insert(1,"Tania")
for alumno in alumnos:
    print(alumno,end = " ")

print()
#para eliminar
alumnos.remove("Hector")
print(alumnos)
#eliminar por su índice
alumnos.pop(2)
print(alumnos)

print()
#listas alumnos 303
alumnos=["addi,alberto,bryan,rebeca,juan,duran,rosa,jenni,tania,hector,paty"]
print(alumnos)
print()

#funcion len
len(alumnos)
print(alumnos)
print()

#funcion sort, ordena alfabeticamente
alumnos.sort()
print(alumnos)

#funcion sort reverse=true
alumnos.sort(reverse=True)
print(alumnos)

