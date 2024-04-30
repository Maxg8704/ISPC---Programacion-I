''' 14- Signo zodiacal. El signo zodiacal de una persona está determinado por su día de
nacimiento.
El diccionario de signos asocia a cada signo el período del año que le corresponde. Cada
período es una tupla con la fecha de inicio y la fecha de término, y cada fecha es una
tupla (mes, dia):
signos = {
'aries': (( 3, 21), ( 4, 20)),
'tauro': (( 4, 21), ( 5, 21)),
'geminis': (( 5, 22), ( 6, 21)),
'cancer': (( 6, 22), ( 7, 23)),
'leo': (( 7, 24), ( 8, 23)),
'virgo': (( 8, 24), ( 9, 23)),
'libra': (( 9, 24), (10, 23)),
'escorpio': ((10, 24), (11, 22)),
'sagitario': ((11, 23), (12, 21)),
'capricornio': ((12, 22), ( 1, 20)),
'acuario': (( 1, 21), ( 2, 19)),
'piscis': (( 2, 20), ( 3, 20)),
}
Por ejemplo, para que una persona sea de signo libra debe haber nacido entre el 24 de
septiembre y el 23 de octubre.
Escriba la función determinar_signo(fecha_de_nacimiento) que reciba como
parámetro la fecha de nacimiento de una persona, representada como una tupla (año,
mes, dia), y que retorne el signo zodiacal de la persona.
'''

def determinar_signo(fecha_de_nacimiento):
    signos = {
        'Aries': ((3, 21), (4, 19)),
        'Tauro': ((4, 20), (5, 20)),
        'Géminis': ((5, 21), (6, 20)),
        'Cáncer': ((6, 21), (7, 22)),
        'Leo': ((7, 23), (8, 22)),
        'Virgo': ((8, 23), (9, 22)),
        'Libra': ((9, 23), (10, 22)),
        'Escorpio': ((10, 23), (11, 21)),
        'Sagitario': ((11, 22), (12, 21)),
        'Capricornio': ((12, 22), (1, 19)),
        'Acuario': ((1, 20), (2, 18)),
        'Piscis': ((2, 19), (3, 20))
    }
    mes, dia = fecha_de_nacimiento[1], fecha_de_nacimiento[2]
    
    for signo, (inicio, fin) in signos.items():
        if (mes == inicio[0] and dia >= inicio[1]) or (mes == fin[0] and dia <= fin[1]):
            return signo
    
    return None

try:
    year = int(input("Ingrese el año de nacimiento: "))
    month = int(input("Ingrese el mes de nacimiento: "))
    day = int(input("Ingrese el día de nacimiento: "))
    fecha_de_nacimiento = (year, month, day)

    signo = determinar_signo(fecha_de_nacimiento)
    if signo:
        print("El signo zodiacal es:", signo)
    else:
        print("No se encontró ningún signo zodiacal para la fecha de nacimiento proporcionada.")
except ValueError:
    print("Ingrese valores numéricos para el año, mes y día.")





