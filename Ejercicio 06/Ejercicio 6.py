''' 6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un
    triángulo rectángulo como el de más abajo con tantos renglones como indique el
    usuario. '''

def imprimir_triangulo(num_filas):
    for i in range(1, num_filas + 1):
        print('*' * i)

def main():
    try:
        num_filas = int(input("Ingrese el número de filas para el triángulo: "))
        if num_filas > 0:
            imprimir_triangulo(num_filas)
        else:
            print("Por favor, ingrese un número mayor que cero.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
 