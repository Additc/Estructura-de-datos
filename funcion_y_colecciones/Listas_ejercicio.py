"""
Nombre: Addi Toro Chavez
Fecha: 12 de noviembre del 2024
Descripción:
Listas ejercicio
"""
from defer import return_value

videos_youtube=[ ]

#Función de menú
def menu( ):
    print("Ingrese una opción:")
    print("1: Ver lista de videos por añadido")
    print("2: Ver lista de videos por orden A-Z")
    print("3: Ver lista de videos por orden Z-A")
    print("4: Añadir video")
    print("5: Añadir varios videos")
    print("6: Eliminar video")
    print("0: Salir")
    opcion=int(input("Ingrese la opción: "))
    return opcion
opcion=menu()

def lista_videos (videos_youtube):
    for a in videos_youtube:
        print(videos_youtube, end = " ")

def orden1_videos(videos_youtube):
    videos_youtube.sort()
    print(videos_youtube)

def orden2_videos(videos_youtube):
    videos_youtube.short(reverse=True)

def añadir_video(videos_youtube):
    videos_youtube.insert()
    print(videos_youtube, end=" ")

def añadir_varios(videos_youtube):
    numero_videos=int(input("ingrese la cantidad de videos que desea agregar: "))
    numero_videos.append()
    for k range numero_videos:
        input("ingrese nombre del video: ")

    return videos_youtube

def eliminar(videos_youtube):
    pos= int(input("inserte el número de la pocisión que desea eliminar: "))
