#MULTIPLICACION RUSA
inicio = 1
while inicio == 1:
    c = int(0)
    multiplicando = int(input('Digite el primer numero: '))
    multiplicador = int(input('Digite el segundo numero: '))
    a = multiplicando
    b = multiplicador

    while(a > 0):

        if (a % 2 != 0):
            c = c + b
        a = int(a / 2)
        b = b * 2

    print(f'El resultado de {multiplicando} * {multiplicador} es = {c}')
    print(" ")
    

