"""
Nombre: Addi Toro Chavez
Fecha: 12 de noviembre del 2024
Descripción:
Listas ejercicio 3 promedios
"""


alumnos=[ ]
calificaciones=[ ]
materias=['Estructura de datos','Álgebra','Contabilidad','ElectrÓnica','Derecho y Legislación','Inglés']
contador_alumnos=0
#Función de menú
def menu( ):
    print()
    print("Seleccione una opción")
    print("1: Ver calificaciones de todos los alumnos")
    print("2: Ver calificaciones de un alumno") # nombre y cantidad
    print("3: Ver promedios del primer parcial de todos los alumnos")
    print("4: Ver promedio grupal del parcial 1")
    print("5: Añadir alumno")
    print("6: Eliminar alumno")
    print("0: Salir")
    opcion=int(input("Ingrese la opción: "))
    return opcion

def ver_calificaciones (alumnos,calificaciones,contador_alumnos):
    contador_alumnos=0
    if len(alumnos)==0:
        print("No hay alumnos")
    else:
        for alumno in alumnos:
            print()
            print(f"{alumno}:{calificaciones[contador_alumnos]}")
            contador_alumnos+=1
            print()

def ver_calificaciones_alumno(alumnos,calificaciones,contador_alumnos,materias):
    contador_alumnos=1
    if len(alumnos)==0:
       print("No hay alumnos")
    else:
        print()
        print("Seleccione un alumno:")
        for alumno in alumnos:
            print(f"{contador_alumnos}._{alumno}")
            contador_alumnos += 1
            print()

        pos=int(input("Ingrese la pocisición del alumno del que desea ver las calificaciones: "))
        print()
        print(f"Alumno seleccionado:{alumnos[pos - 1]}")
        for materia,calificacion in zip (materias,calificaciones[pos-1]):
            print(f"{materia}:{calificacion}", end = " ")
            print()
def ver_promedio_alumnos(alumnos,calificaciones,contador_alumnos, materias):
    contador_alumnos=1
    if len(alumnos)==0:
        print("No hay alumnos")
    else:
        promedio=[]
        for calificacion, alumno in zip (calificaciones,alumnos):
            promedio=(sum(calificacion))/len(calificacion)
            print(f"Alumno:{alumno} promedio: {promedio}")


def promedio_grupal(alumnos, califiaciones,contador_alumnos):
    contador_alumnos=1
    if len(alumnos)==0:
        print("No hay alumnos")
    else:
        promedio_g=0
        total_calificaciones=0
        for calificacion, alumno in zip (calificaciones,alumnos):
            total_calificaciones=(sum(calificacion))
            promedio_g= total_calificaciones/len(calificacion)
        print(f"El promedio grupal de alumnos es:  {promedio_g}")



def anadir ( alumnos,calificaciones):
        alumno = input("Ingresa al nuevo alumno: ")
        alumnos.append(alumno)
        estructura = float(input("Ingresa la calificación de la materia de Estructura de Datos: "))
        algebra = float(input("Ingresa la calificación de la materia de Álgebra: "))
        contabilidad = float(input("Ingresa la calificación de la materia de Contabilidad: "))
        electronica = float(input("Ingresa la calificación de la materia de Electrónica: "))
        derecho = float(input("Ingresa la calificación de la materia de Derecho y Legislación: "))
        ingles = float(input("Ingresa la calificación de la materia de Inglés: "))
        calificaciones.append([estructura,algebra,contabilidad,electronica,derecho,ingles])

def eliminar (alumnos,calificaciones,contador_alumnos):
    contador_alumnos=1
    if len(alumnos)==0:
       print("No hay alumnos")
    else:
        print()
        print("Seleccione un alumno:")
        for alumno in alumnos:
            print(f"{contador_alumnos}._{alumno}")
            contador_alumnos += 1
            print()

        pos=int(input("Ingrese la pocisición del alumno del que desea eliminar: "))
        print()
        print(f"Alumno seleccionado:{alumnos[pos - 1]}")
        print("Alumno eliminado")
        alumnos.pop(pos-1)
        calificaciones.pop(pos-1)
        contador_alumnos-=1
        print()

op=1
while op !=0:
    opcion=menu()
    if opcion ==1:
        ver_calificaciones(alumnos,calificaciones,contador_alumnos)
    elif opcion==2:
        ver_calificaciones_alumno(alumnos,calificaciones,contador_alumnos,materias)
    elif opcion==3:
        ver_promedio_alumnos(alumnos,calificaciones, contador_alumnos,materias)
    elif opcion==4:
        promedio_grupal(alumnos, calificaciones, contador_alumnos)
    elif opcion ==5:
        anadir(alumnos,calificaciones)
        contador_alumnos += 1
    elif opcion ==6:
        eliminar(alumnos, calificaciones, contador_alumnos)
    elif opcion == 0:
        op=0
        print("Salió del programa")
else:
    print("opción incorrecta")

"""
Declaro 3 listas, una que me ayudará con la manipulación de las calificaciones, otra con los nombres de los alumnos y una
última que garda el nombre de mis materias, además de un contador para conocer la cantidad de alumnos.

Defino mis funciones a utilizar, mandando a cada una de ellas las 2 o 3 listas declaradas previamente, según sea el caso
a realizar, e implemento la lógica necesaria dentro de las funciones.

Establezco  mis opciones del menú dentro de un ciclo while con las declaraciones de las condiciones,
y según sea el caso mando a llamar a la función correspondiente. 
"""