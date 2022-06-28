def suma(a, b):
    return a + b
#c = suma(5, 550)
print(suma(5, 550))


#MUTABLE
v = [1,2,3]
def modificar_v(z):
    z.append(4)
    return z
print(modificar_v(v))
print(v)

#INMUTABLE
y = 2
def modificar_y(x):
    x += 20
    return x
print(modificar_y(y))
print(y)

def dias_mes(mes):
    if mes == 12 or mes == 7:
        return 31
    elif mes ==4 or mes ==6:
        return 30
    elif mes == 2:
        return 28
    else:
        return 0
print(dias_mes(12))

def aritme(a, b):
    return f"Suma: {a+b} | Resta: {a-b} | Multiplicacion: {a*b} | Division: {a/b}"
print(aritme(12,2))

lista = list(aritme(10,5))