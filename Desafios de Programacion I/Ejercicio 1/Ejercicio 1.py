''' 1- Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso. '''

def invertir_numero(numero):
    numero_str = str(numero)
    numero_invertido = numero_str[::-1]
    return int(numero_invertido)

numero1 = 345
numero2 = 241
resultado1 = invertir_numero(numero1)
resultado2 = invertir_numero(numero2)

print("El número", numero1, "invertido es:", resultado1)
print("El número", numero2, "invertido es:", resultado2)
