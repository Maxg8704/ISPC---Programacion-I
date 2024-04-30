##
* 13 - El diccionario países asocia cada persona con el conjunto de los países que ha
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
##