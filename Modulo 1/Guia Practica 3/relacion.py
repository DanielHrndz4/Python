def relacion(a, b):
    if n1 > n2:
        return 1
    elif n1 < n2:
        return -1
    elif n1 == n2:
        return 0

n1 = input("Digite el primer numero: ")
n2 = input("Digite el segundo numero: ")
print('Resultado:',relacion(n1, n2))