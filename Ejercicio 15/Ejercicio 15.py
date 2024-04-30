''' 15 - Autores de Libros. Este problema apareció en el certamen 2 del segundo semestre de
2011 en el campus Vitacura.
Escriba las funciones necesarias para que el siguiente programa funcione:
9libros = [
('Papelucho programador', 'Marcela Paz', 1983),
('Don Python de la Mancha', 'Miguel de Cervantes', 1615),
('Raw_input y Julieta', 'William Shakespeare', 1597),
('La tuplamorfosis', 'Franz Kafka', 1915),

]
autores = {
# autor: nacimiento, defunción, idioma
'William Shakespeare': ((1564, 4, 26), (1616, 5, 3), 'inglés'),
'Franz Kafka': ((1883, 7, 3), (1924, 6, 3), 'alemán'),
'Marcela Paz': ((1902, 2, 28), (1985, 6, 12), 'español'),
'Miguel de Cervantes': ((1547, 9, 29), (1616, 4, 22), 'español'),

}
titulo = input('Ingrese titulo del libro: ')
print 'El libro fue escrito en', obtener_idioma(titulo),
print 'por', obtener_autor(titulo)
print 'El autor fallecio', calcular_annos_antes_de_morir(titulo), 'años',
print 'después de haber escrito el libro' '''

libros = [
    ('Papelucho programador', 'Marcela Paz', 1983),
    ('Don Python de la Mancha', 'Miguel de Cervantes', 1615),
    ('Raw_input y Julieta', 'William Shakespeare', 1597),
    ('La tuplamorfosis', 'Franz Kafka', 1915),
]

autores = {
    'William Shakespeare': ((1564, 4, 26), (1616, 5, 3), 'inglés'),
    'Franz Kafka': ((1883, 7, 3), (1924, 6, 3), 'alemán'),
    'Marcela Paz': ((1902, 2, 28), (1985, 6, 12), 'español'),
    'Miguel de Cervantes': ((1547, 9, 29), (1616, 4, 22), 'español'),
}

def obtener_idioma(titulo):
    for libro in libros:
        if libro[0] == titulo:
            autor = libro[1]
            return autores[autor][2]
    return "No se encontró el libro en la lista."

def obtener_autor(titulo):
    for libro in libros:
        if libro[0] == titulo:
            return libro[1]
    return "No se encontró el libro en la lista."

def calcular_annos_antes_de_morir(titulo):
    for libro in libros:
        if libro[0] == titulo:
            autor = libro[1]
            fecha_publicacion = libro[2]
            fecha_muerte = autores[autor][1]
            años_después = fecha_publicacion - fecha_muerte[0]
            return años_después
    return "No se encontró el libro en la lista."

titulo = input('Ingrese título del libro: ')
print('El libro fue escrito en', obtener_idioma(titulo),
      'por', obtener_autor(titulo))
print('El autor falleció', calcular_annos_antes_de_morir(titulo), 'años',
      'después de haber escrito el libro')

