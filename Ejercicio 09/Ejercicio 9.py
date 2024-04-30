''' 9 - Anagrama. Escribe una función que reciba dos palabras y retorne
verdadero o falso según sean o no anagramas.
● Un Anagrama consiste en formar una palabra reordenando TODAS las letras de
otra palabra inicial.
● NO hace falta comprobar que ambas palabras existen.
● Dos palabras exactamente iguales no son anagrama. '''

def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    if len(palabra1) != len(palabra2):
        return False
    
    contador_letras = {}
    for letra in palabra1:
        if letra in contador_letras:
            contador_letras[letra] += 1
        else:
            contador_letras[letra] = 1
    
    for letra in palabra2:
        if letra in contador_letras:
            contador_letras[letra] -= 1
        else:
            return False
    
    for count in contador_letras.values():
        if count != 0:
            return False
    return True

palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

if son_anagramas(palabra1, palabra2):
    print("Las palabras son anagramas.")
else:
    print("Las palabras no son anagramas.")
