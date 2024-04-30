''' 12- Torneo de Tenis. Escriba un programa para simular un campeonato de tenis.
Primero, debe pedir al usuario que ingrese los nombres de ocho tenistas. A continuación,
debe pedir los resultados de los partidos juntando los jugadores de dos en dos. El
ganador de cada partido avanza a la ronda siguiente.
El programa debe continuar preguntando ganadores de partidos hasta que quede un
único jugador, que es el campeón del torneo. '''

def solicitar_ganador(partido):
    print(f"Ingrese el ganador del partido {partido}: ")
    return input().strip()

def jugar_torneo():
    tenistas = [input(f"Ingrese el nombre del tenista {i+1}: ") for i in range(8)]
    
    enfrentamientos = [(tenistas[0], tenistas[1]), (tenistas[2], tenistas[3]), 
                       (tenistas[4], tenistas[5]), (tenistas[6], tenistas[7])]
    
    while len(enfrentamientos) > 1:
        ganadores = []
        for i in range(0, len(enfrentamientos), 2):
            ganador1 = solicitar_ganador(enfrentamientos[i])
            ganador2 = solicitar_ganador(enfrentamientos[i+1])
            ganadores.append(ganador1 if ganador1 else ganador2)
        enfrentamientos = [(ganadores[i], ganadores[i+1]) for i in range(0, len(ganadores), 2)]
    
    print(f"¡{enfrentamientos[0][0]} es el campeón del torneo de tenis!")

jugar_torneo()
