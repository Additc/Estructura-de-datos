'''
Nombre: Addi Toro Chavez
Fecha: 21 de enero de 2025.
Descripción: Argumentos variables kwargs
'''

def prefenrencias (tema:str,**kwargs): # función qu recibe como diccionario
    print(f"El tema es {tema}")
    for key,value in kwargs.items():
        print(f"Nombre: {key} prefiere: {value}")


if __name__ == '__main__':
    #argumentos variables en forma de diccionario
    prefenrencias("comida", rebeca="mole",juan="tacos",bryan="tlayudas",yamm="tamales")