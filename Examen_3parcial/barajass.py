import random


# Definir la clase para la baraja española
class BarajaEspañola:
    def __init__(self):
        # La baraja tiene 4 palos (oros, copas, espadas, bastos) y 12 valores (1 al 12)
        self.palos = ['Oros', 'Copas', 'Espadas', 'Bastos']
        self.cartas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        self.baraja = [f'{carta} de {palo}' for palo in self.palos for carta in self.cartas]

    def barajar(self):
        random.shuffle(self.baraja)

    def repartir_caballos(self):
        # El jugador seleccionará un caballo al azar de la baraja (el 10 de cada palo)
        caballos = [carta for carta in self.baraja if '10' in carta]
        random.shuffle(caballos)
        return caballos[0], caballos[1]  # Se le asigna un caballo a cada jugador


# Función para simular la carrera
def simular_carrera(jugador1, jugador2):
    meta = 100  # Distancia de la carrera
    avance1, avance2 = 0, 0
    turno = 1

    print(f"\nComienza la carrera: {jugador1} contra {jugador2}!\n")
    while avance1 < meta and avance2 < meta:
        # Avance al azar de cada jugador
        avance1 += random.randint(1, 10)  # Jugador 1 avanza entre 1 y 10
        avance2 += random.randint(1, 10)  # Jugador 2 avanza entre 1 y 10

        print(f"Turno {turno}:")
        print(f"{jugador1} avanza a {avance1} metros.")
        print(f"{jugador2} avanza a {avance2} metros.")

        turno += 1
        if avance1 >= meta:
            print(f"\n¡{jugador1} ha ganado la carrera!")
        elif avance2 >= meta:
            print(f"\n¡{jugador2} ha ganado la carrera!")


# Función principal
def juego():
    baraja = BarajaEspañola()
    baraja.barajar()

    # Repartir caballos a los jugadores
    jugador1_caballo, jugador2_caballo = baraja.repartir_caballos()
    jugador1 = f"Jugador 1 con {jugador1_caballo}"
    jugador2 = f"Jugador 2 con {jugador2_caballo}"

    # Iniciar la carrera
    simular_carrera(jugador1, jugador2)


# Ejecutar el juego
if __name__ == "__main__":
    juego()
