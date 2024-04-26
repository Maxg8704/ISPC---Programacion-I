''' 3- Escribir un programa que pida al usuario un número entero y muestre por pantalla si
    es un número primo o no. '''

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def verificar_primo():
    while True:
        try:
            numero = int(input("Por favor, introduce un número entero para verificar si es primo: "))
            if numero < 0:
                print("Por favor, introduce un número entero positivo.")
                continue
            if es_primo(numero):
                print(f"{numero} es un número primo.")
            else:
                print(f"{numero} no es un número primo.")
            break
        except ValueError:
            print("Por favor, introduce un número entero válido.")

verificar_primo()



