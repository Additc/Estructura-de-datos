"""
Nombre: Addi Toro Chavez
Fecha: 12 de noviembre del 2024
Descripción:
Listas ejercicio
"""

videos_youtube=[ ]
contador =0
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
    return videos_youtube

def orden2_videos(videos_youtube):
    videos_youtube.short(reverse=True)
    return videos_youtube

def añadir_video(videos_youtube):
    contador =0
    videos_youtube.insert()
    contador += 1
    return videos_youtube

def añadir_varios(videos_youtube):
    contador=0
    n=int(input("ingrese la cantidad de videos que desea agregar: "))
    for i in  range(n):
        nombre_video=input("ingrese nombre del video: ")
        contador+=1
        videos_youtube.append(nombre_video)
    return videos_youtube , contador

def eliminar(videos_youtube, contador):
    if contador == 0:
        print("No hay videos")
    else:
        pos=int(input("Ingrese la pocisión del video que desea eliminar: "))
        videos_youtube.pop(pos)
    return videos_youtube


