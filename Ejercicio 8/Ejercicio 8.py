''' 8- Este problema apareció en el certamen recuperativo 1 del segundo semestre de 2011
en el campus Vitacura.
Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen
respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10,
$50 y $100.
Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las
monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio
del producto, el programa debe entregar las monedas de vuelto, una por una. '''

def vending_machine():
    precios = {'A': 270, 'B': 340, 'C': 390}
    monedas = [10, 50, 100]
    
    producto = input("Elija el producto (A, B o C): ").upper()
    
    if producto not in precios:
        print("Producto inválido.")
        return
    
    precio_producto = precios[producto]
    
    monto_ingresado = 0
    while monto_ingresado < precio_producto:
        try:
            moneda = int(input("Ingrese una moneda (10, 50 o 100): "))
        except ValueError:
            print("Debe ingresar un valor numérico.")
            continue
        if moneda not in monedas:
            print("Moneda inválida.")
            continue
        monto_ingresado += moneda
    
    vuelto = monto_ingresado - precio_producto
    
    print("Vuelto:")
    for m in reversed(monedas):
        while vuelto >= m:
            print(m)
            vuelto -= m

vending_machine()
