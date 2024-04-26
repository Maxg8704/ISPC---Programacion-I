''' La secuencia de Collatz de un número entero se construye de la siguiente forma:

● si el número es par, se lo divide por dos;
● si es impar, se le multiplica tres y se le suma uno;
● La sucesión termina al llegar a uno.

Desarrolle un programa que entregue la secuencia de Collatz de un número entero: '''

def collatz_sequence(numero):
    secuencia = [numero]  # Inicializamos la secuencia con el número dado
    
    while numero != 1:  # Continuamos hasta que lleguemos a 1
        if numero % 2 == 0:  # Si es par
            numero //= 2
        else:  # Si es impar
            numero = numero * 3 + 1
        secuencia.append(numero)  # Agregamos el número a la secuencia
    
    return secuencia

# Ejemplo de uso
numero = int(input("Ingrese un número entero para obtener su secuencia de Collatz: "))
print("La secuencia de Collatz para el número", numero, "es:", collatz_sequence(numero))
