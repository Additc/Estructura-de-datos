"""
Nombre: Addi Toro Chavez
Fecha: 16 de noviembre del 2024
Descripción:
Tuplas ejercicio de coordenadas
"""
coordenadas=[]
contador_coordenadas=0
def menu():
    print()
    print("Seleccione un opción:")
    print("1) Ver coordenadas almacenadas")
    print("2) Agregar coordenada (x,y)")
    print("3) Calcular la pendiente de la recta entre dos coordenadas")
    print("4) Eliminar coordenada (x,y)")
    print("0) Salir")
    opcion=int(input("Seleccione una opción: "))
    return opcion

def ver_coordenadas(coordenadas,contador_coordenadas):
    contador_coordenadas=1
    if len(coordenadas)==0:
        print("No hay coordenadas")
    else:
        for x,y in coordenadas:
            print(f"Coordenada{contador_coordenadas}: {x,y}")
            contador_coordenadas+=1
        print()


def agregar(coordenadas):
    x=float(input("Ingrese el valor de la coordenada x: "))
    y=float(input("Ingrese el valor de la coordenada y: "))
    coordenadas.append((x,y))
    return x,y

def calcular_pend(coordenadas,contador_coordenadas):
    if len(coordenadas) < 2:
        print("No es posible realizar el cálculo")
    else:
        punto1 = int(input("Elija el índice de la primera coordenada: "))
        punto2 = int(input("Elija el índice de la segunda coordenada: "))
        punto1 -= 1
        punto2 -= 1
        if punto1 >=0 and punto2 >= 0 and punto1 <= len(coordenadas) and punto2 <= len(coordenadas):
            x1,y1 = coordenadas[punto1]
            x2,y2 = coordenadas[punto2]
            m = (y2 - y1) / (x2 - x1)
            b = y1 - m * x1
            print(f"La pendiente entre las coordenadas {coordenadas[punto1]} y {coordenadas[punto2]} es: {(m):.2f}")
            print(f"La ecuación de la recta es y= {m}x + ({b})")
        else:
            print("Acción incorrecta")
    print()

def eliminar(coordenadas,contador_coordenadas):
    if len(coordenadas) == 0:
        print("No hay coordenadas.")
    else:
        pos= int(input("Elija el índice de la coordenada que desea eliminar: "))
        if pos >= 0 and pos <= len(coordenadas):
            coordenadas.pop(pos - 1)
            contador_coordenadas -= 1
            print("Coordenada eliminada.")
    print()

op=1
while op!=0:
    opcion=menu()
    if opcion == 1:
        ver_coordenadas(coordenadas,contador_coordenadas)
    elif opcion == 2:
        agregar(coordenadas)
        contador_coordenadas+=1
    elif opcion == 3:
        calcular_pend(coordenadas,contador_coordenadas)
    elif opcion == 4:
        eliminar(coordenadas,contador_coordenadas)
    elif opcion == 0:
        print("Salió del programa")
    else:
        print("opción incorrecta")

"""
Declaro mi lista que me ayudrá a almacenar las coordenadas proporcionadas por el ususario.

Defino mis funciones a ocupar dentro del código, para ver coordenadas, agregar, calcular la pendiente y elimina, posteriormente envío 
la lista declarada a cada una de las fnciones e implemento la lógica a cada una de ellas con ayuda de ciclos y condiciones.

Con una condición while, establezco mis demás condiciones de opciones del menú y mando a llamar las funciones según corrsponda en cada caso.  
"""

