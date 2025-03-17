

import time
import sys

def animacion_texto_desplazado(mensaje, velocidad=0.1, largo_terminal=50):
    mensaje_expandido = mensaje + " " * largo_terminal  # Agregar espacio para el desplazamiento
    while True:
        for i in range(len(mensaje_expandido) - largo_terminal + 1):
            sys.stdout.write(f"\r{mensaje_expandido[i:i+largo_terminal]}")
            sys.stdout.flush()
            time.sleep(velocidad)

mensaje = "Este es un texto largo que se desplazará de izquierda a derecha de forma animada."
animacion_texto_desplazado(mensaje, velocidad=0.1, largo_terminal=100)

"    |\            "
"    | \           "
"    |__\          "
" ___|____________ "
"  \\    o o    /  "
"~~~~~~~~~~~~~~~~~~~~~~"

"     |\ /\   "
"     \ 0 0   "
"     / \-_-\ "
"    /-----/  "
"  "
"  _______     "
" |/      |     "
" |      O     "
" |     /|\    "
" |      |      "
" |     / \     "
"_|___         "