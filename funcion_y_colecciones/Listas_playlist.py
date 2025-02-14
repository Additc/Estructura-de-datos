"""
Nombre: Addi Toro Chavez
Fecha: 12 de noviembre del 2024
Descripción:
Listas ejercicio
"""

videos_youtube=[ ]
contador_videos =0
#Función de menú
def menu( ):
    print()
    print("Seleccione una opción")
    print("1: Ver lista de videos por añadido")
    print("2: Ver lista de videos por orden A-Z")
    print("3: Ver lista de videos por orden Z-A")
    print("4: Añadir video")
    print("5: Añadir varios videos")
    print("6: Eliminar video")
    print("0: Salir")
    opcion=int(input("Ingrese la opción: "))
    return opcion

def lista_videos (videos_youtube,contador_videos):
    contador_videos=1
    for videos in videos_youtube:
        print(f"{contador_videos}._{videos}", end=" ")
        contador_videos+=1
    print()
def orden1_videos(videos_youtube):
    videos_youtube.sort()
    print("Ordenado alfabéticamente correctamente")

def orden2_videos(videos_youtube):
    videos_youtube.sort(reverse=True)
    print("Ordenado de manera inversa correctamente")

def añadir_video(videos_youtube):
    video=input("Ingrese nombre del video: ")
    videos_youtube.append(video)

def añadir_varios(videos_youtube,contador_videos):
    n=int(input("ingrese la cantidad de videos que desea agregar: "))
    for i in  range(n):
        videos=input("ingrese nombre del video: ")
        videos_youtube.append(videos)
        contador_videos+=1

def eliminar(videos_youtube,contador_videos):
        pos=int(input("Ingrese la pocisión del video que desea eliminar: "))
        videos_youtube.pop(pos-1)
        contador_videos-=1
        print("Video eliminado")


op=1
while op !=0:
    opcion=menu()
    if opcion==1:
        lista_videos(videos_youtube,contador_videos)
    elif opcion==2:
        orden1_videos(videos_youtube)
    elif opcion ==3:
        orden2_videos(videos_youtube)
    elif opcion == 4:
        añadir_video(videos_youtube)
        contador_videos+=1
    elif opcion == 5:
        añadir_varios(videos_youtube,contador_videos)
    elif opcion == 6:
        eliminar(videos_youtube,contador_videos)
    elif opcion == 0:
        op=0
        print("Salió del programa")
else:
    print("opción incorrecta")

"""
Declaro una lista que almacenará el nombre de los videos, y también un contador para conocer el número de estos.
Defino mis funciones para las distintas opciones del menú, recibiendo en ellas dependiendo el caso la lista y el contador
de videos.
Se implementa la lógica necesaria con las funciones (pop, sort, appent) en cada una de ellas.

Establezco mi ciclo while y dentro de él establezco mis condiciones de acuerdo a las opciones y llamo a las funciones
previamente definidas en donde corresponden. 
"""