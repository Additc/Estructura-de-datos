"""
Nombre: Addi Toro Chavez
Fecha: 2 de diciembre del 2024
Descripción:
Diccionario
"""


#es tambien ordenado, ingresado con una par-clave o valor
print("**Ejemplos de uso**")

#para crear diccionario
diccionario_profesor = {'nombre':"Adalberto",'primer apellido':"Matinez",'edad':31,'correo':"adalberto.mtba@unsij.ed.mx",'cubo':12}
print(diccionario_profesor)
print()
diccionario_alumno={'nombre':"Addi",'apellido':"toro",'apellido2':"chavez",'grupo':"303",'materiafavorita':"estructura" }
print(diccionario_alumno)
print()

# para ingresar elemntos
diccionario_alumno['nombre']="Addi"
diccionario_alumno['apellido']="Toro"

#Se accede a los elementos del diccionario
nombre_nombre=diccionario_alumno.get('nombre')
diccionario_apellido=diccionario_alumno.get('apellido')

#Se modifican elementos
diccionario_alumno['nombre']="Alberto"
diccionario_alumno['apellido']="chavez"
print(diccionario_alumno)
print()

#Se elimina el par clave-valor
del diccionario_alumno['apellido2']
diccionario_alumno.pop('grupo')


#Se accede al par clave-valor
for clave, valor in diccionario_alumno.items():
    print(f"clave: {clave} y valor: {valor}")

#para el puro valor
for clave in diccionario_alumno.values():
    print(f"{clave}")

#para las claves
for clave in diccionario_alumno.keys():
    print(f"{clave}")

#combinacion con tuplas
diccionario_egresado={'nombre':"uriel",('primer_a''segundo_a'):"Uriel perez",'edad':23}
print(diccionario_egresado)
for clave in diccionario_egresado.values():
    print(f"{clave}")
for clave in diccionario_egresado.keys():
    print(f"{clave}")

diccionario_informatica={'grupo_303':{'n_alumnos':12,'n_materias':5,'promedio_grupal':7.9},
                         'grupo_503':{'n_alumnos':9,'n_materias':5,'promedio_grupal':8},
                         'grupo_703':{'n_alumnos':9,'n_materias':5,'promedio_grupal':8},
                         'grupo_903':{'n_alumnos':9,'n_materias':5,'promedio_grupal':8}}

for grupo in enumerate(diccionario_informatica):
    print(f"grupo:{grupo}")

#acceder a los elementos
prom_303=diccionario_informatica['grupo_303']['prmedio_grupal']