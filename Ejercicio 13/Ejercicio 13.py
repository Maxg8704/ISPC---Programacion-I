''' 13 - El diccionario países asocia cada persona con el conjunto de los países que ha
visitado:
paises = {
'Pepito': {'Chile', 'Argentina'},
'Yayita': {'Francia', 'Suiza', 'Chile'},
'John': {'Chile', 'Italia', 'Francia', 'Peru'},
}

Escriba una función cuantos en comun(a, b), que indique cuántos países en común han
visitado la persona a y la persona b:

>>> cuantos en comun('Pepito', 'John')
1
>>> cuantos en comun('John', 'Yayita')
2
'''

def cuantos_en_comun(a, b):
    paises = {
        'Pepito': {'Chile', 'Argentina'},
        'Yayita': {'Francia', 'Suiza', 'Chile'},
        'John': {'Chile', 'Italia', 'Francia', 'Peru'},
    }
    
    if a not in paises or b not in paises:
        return "Una de las personas no está en el diccionario."
    paises_a = paises[a]
    paises_b = paises[b]
    
    paises_en_comun = paises_a.intersection(paises_b)
    
    return len(paises_en_comun)

print(cuantos_en_comun('Pepito', 'John'))  
print(cuantos_en_comun('John', 'Yayita'))  




