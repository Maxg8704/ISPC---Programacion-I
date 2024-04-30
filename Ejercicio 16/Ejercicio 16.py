''' 16- Código Morse. Crea un programa que sea capaz de transformar texto natural a
código morse y viceversa.
● Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
● En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos
espacios entre palabras " ".
● El alfabeto morse soportado será el mostrado en
https://es.wikipedia.org/wiki/Código_morse '''

# Diccionario que mapea caracteres a su representación en código Morse
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

# Diccionario inverso que mapea representaciones en código Morse a caracteres
morse_to_char = {value: key for key, value in morse_code.items()}

def texto_a_morse(texto):
    if not texto:
        return ""
    if texto[0] in morse_code:
        return " ".join(morse_code[char.upper()] for char in texto)
    else:
        return "   ".join(texto.split())

def morse_a_texto(morse):
    if not morse:
        return ""
    palabras = morse.split("   ")
    texto = ""
    for palabra in palabras:
        letras = palabra.split(" ")
        for letra in letras:
            if letra in morse_to_char:
                texto += morse_to_char[letra]
        texto += " "
    return texto.strip()

def main():
    entrada = input("Ingrese texto o código Morse: ")
    if '-' in entrada or '.' in entrada:
        resultado = morse_a_texto(entrada)
        print("Texto:", resultado)
    else:
        resultado = texto_a_morse(entrada)
        print("Código Morse:", resultado)

if __name__ == "__main__":
    main()

