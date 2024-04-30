''' 11- Piedra, papel y tijera. En cada ronda del juego del cachipún, los dos competidores
deben elegir entre jugar tijera, papel o piedra.
Las reglas para decidir quién gana la ronda son: tijera le gana a papel, papel le gana a
piedra, piedra le gana a tijera, y todas las demás combinaciones son empates.
El ganador del juego es el primero que gane tres rondas.
Escriba un programa que pregunte a cada jugador cuál es su jugada, muestre cuál es el
marcador después de cada ronda, y termine cuando uno de ellos haya ganado tres
rondas. Los jugadores deben indicar su jugada escribiendo tijera, papel o piedra. '''

def obtener_ganador(jugada1, jugada2):
    if jugada1 == jugada2:
        return "Empate"
    elif (jugada1 == "piedra" and jugada2 == "tijera") or \
         (jugada1 == "tijera" and jugada2 == "papel") or \
         (jugada1 == "papel" and jugada2 == "piedra"):
        return "Jugador 1"
    else:
        return "Jugador 2"

# Marcador
marcador_jugador1 = 0
marcador_jugador2 = 0

# Juego
while marcador_jugador1 < 3 and marcador_jugador2 < 3:
    jugada_jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
    jugada_jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()
    
    if jugada_jugador1 not in ["piedra", "papel", "tijera"] or jugada_jugador2 not in ["piedra", "papel", "tijera"]:
        print("Jugada inválida. Por favor, elige piedra, papel o tijera.")
        continue
    
    ganador = obtener_ganador(jugada_jugador1, jugada_jugador2)
    
    if ganador == "Jugador 1":
        marcador_jugador1 += 1
    elif ganador == "Jugador 2":
        marcador_jugador2 += 1
    
    print(f"Marcador: Jugador 1 ({marcador_jugador1}) - Jugador 2 ({marcador_jugador2})")

# Ganador del juego
if marcador_jugador1 == 3:
    print("¡El Jugador 1 ha ganado el juego!")
else:
    print("¡El Jugador 2 ha ganado el juego!")
