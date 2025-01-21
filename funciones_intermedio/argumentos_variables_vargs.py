'''
Nombre: Addi Toro Chavez
Fecha: 21 de enero de 2025.
Descripción: Argumentos variables vargs
'''


def colores_favoritos(persona:str,*vargs):
    print(f"{persona}: {vargs}")

def sumar(*vargs)->int:
    resultado=0
    for i in vargs:
        resultado+=i

    return resultado # otra manera seria return sum(vargs)



if __name__ == '__main__':
    colores_favoritos("Jennifer","morado","negro","blanco","rosa")
    colores_favoritos("Addi","azul","blanco","negro",)
    colores_favoritos("lobetho",  "negro")
    cadena="hola"
    tupla=("hola",)
    print()
    print(f"cadena {cadena}, tupla {tupla}")
    print()
    res=sumar(5,3,4)
    print(f"el resultado es: {res}")