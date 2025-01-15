'''
Nombre: Addi Toro Chavez
Fecha: 15 de enero de 2025.
Descripción: Argumentos por nombre
'''



def imprimir_alumno(nombre:str,edad:int,matricula:int,grupo:int,semestre:int):
    print(f"Datos personales"
          f"Nombre: {nombre}"
          f"Edad: {edad}"
          f"Matrícula: {matricula}"
          f"Grupo: {grupo}"
          f"Semestre: {semestre}")



def main ()->None:
    nombre="Addi"
    edad= 19
    matricula=11042005
    grupo= 303
    semestre=3
    imprimir_alumno(nombre,edad,matricula,grupo,semestre)


if __name__ == '__main__':
    main()
