def descuento(a, b):
    return producto * 0.1
def iva(a):
    return producto * 0.13
def diccionario():
    d1 = {
        'producto' : 'camisa',
        'iva': iva(producto),
        'descuento': descuento(producto)
    }
    print(d1)
    d2 = {
        'producto' : 'pantalon',
        'iva': iva(producto1),
        'descuento': descuento(producto1)
    }
    print(d2)
    print(" ")
    print(d1 + d2)

producto = int(input('Digite el precio: '))
producto1 = int(input('Digite el precio: '))
print(descuento())
