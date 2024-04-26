''' 2- Escriba un programa que pregunte al usuario la hora actual t del reloj y un número
    entero de horas h, que indique qué hora marcará el reloj dentro de h horas: '''

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



