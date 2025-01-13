'''
Nombre: Addi Toro Chavez
Fecha: 8 de enero de 2025.
Descripción: Saludar módulo
'''

def saludar (nombre:str)-> None:
    print(f"hola {nombre}")

#código que irá a nivel de módulo a partir de ahora
if __name__ == '__main__':
    nombre_cadena = input("ingrese nombre: ")
    nombre = saludar(nombre_cadena)