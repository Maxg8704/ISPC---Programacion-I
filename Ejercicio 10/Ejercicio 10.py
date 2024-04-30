''' 10- Torre y Alfil. Un tablero de ajedrez es una grilla de ocho filas y ocho columnas,
numeradas de 1 a 8. Dos de las piezas del juego de ajedrez son el alfil y la torre. El alfil se
desplaza en diagonal, mientras que la torre se desplaza horizontal o verticalmente. Una
pieza puede ser capturada por otra si está en una casilla a la cual la otra puede
desplazarse:
Escriba un programa que reciba como entrada las posiciones en el tablero de un alfil y de
una torre, e indique cuál pieza captura a la otra: '''

def captura_pieza(alfil, torre):
    alfil_fila, alfil_columna = alfil
    torre_fila, torre_columna = torre
    
    if alfil_fila == torre_fila or alfil_columna == torre_columna:
        return "Torre"
    
    if abs(alfil_fila - torre_fila) == abs(alfil_columna - torre_columna):
        return "Alfil"
    
    return "Ninguna"

try:
    alfil_posicion = tuple(map(int, input("Ingrese la posición del alfil (fila columna): ").split()))
    torre_posicion = tuple(map(int, input("Ingrese la posición de la torre (fila columna): ").split()))

    pieza_capturadora = captura_pieza(alfil_posicion, torre_posicion)

    if pieza_capturadora == "Ninguna":
        print("Ninguna pieza captura a la otra.")
    else:
        print(f"La {pieza_capturadora} captura a la otra.")
except ValueError:
    print("Ingrese posiciones válidas (números enteros separados por espacios).")

