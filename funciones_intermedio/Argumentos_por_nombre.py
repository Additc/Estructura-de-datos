'''
Nombre: Addi Toro Chavez
Fecha: 15 de enero de 2025.
Descripción: Argumentos por nombre
'''


def imprimir_alumno(nombre:str,edad:int,matricula:int,grupo:int,semestre:int):#Se puede epecificar en la función
    """
    Función que muestra los datos personales del alumno.
    :param nombre: Nombre de un alumno
    :param edad: Edad del alumno
    :param matricula: Matrícula de un alumno
    :param grupo:Grupo del alumno
    :param semestre: Semestre del alumno
    :return:
    """
    print(f"Datos personales\n"
              f"Nombre: {nombre}\n"
              f"Edad: {edad}\n"
              f"Matrícula: {matricula}\n"
              f"Grupo: {grupo}\n"
              f"Semestre: {semestre}")



def main ()->None:
    """
    Función main
    :return:
    """
    nombre="Addi"
    edad= 19
    matricula=11042005
    grupo=303
    semestre=3
    imprimir_alumno(nombre,edad,matricula,grupo,semestre)
    print()
    print("Argumentos cambiados por nombre")
    imprimir_alumno(nombre="Addi", matricula=19,edad=11042005,grupo=3,semestre=303) #Argumentos por nombre

if __name__ == '__main__':
    main()
