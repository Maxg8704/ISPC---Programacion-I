''' 4- Tiempo de viaje. Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él
    tiene la duración en minutos de cada uno de los tramos del viaje.
    Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y
    entregue como resultado el tiempo total de viaje en formato horas:minutos.
    El programa deja de pedir tiempos de viaje cuando se ingresa un 0. '''


def calcular_tiempo_viaje():
    total_minutos = 0
    
    while True:
        duracion_tramo = int(input("Duración tramo: "))
        if duracion_tramo == 0:
            break
        total_minutos += duracion_tramo
    
    horas = total_minutos // 60
    minutos = total_minutos % 60
    
    return horas, minutos

def main():
    horas, minutos = calcular_tiempo_viaje()
    print(f"Tiempo total de viaje: {horas}:{minutos:02d} horas")

if __name__ == "__main__":
    main()
