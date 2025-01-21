'''
Nombre: Addi Toro Chavez
Fecha: 8 de enero de 2025.
Descripción: Saludar main
'''
from saludar_modulo import saludar

if __name__ == '__main__':# verifica que se ejecute el archivo actual
    nombre = input("ingrese nombre: ")
    saludar(nombre)
    print(saludar.__name__)