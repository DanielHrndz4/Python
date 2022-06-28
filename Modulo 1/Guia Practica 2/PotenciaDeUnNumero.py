#POTENCIA DE UN NUMERO
inicio = True
while inicio == True:
    numero = int(input("Ingrese un numero: "))
    potencia = int(input("Ingrese la potencia a multiplicar: "))

    if potencia == 0:
        resultado = numero
    elif numero == 0:
        resultado = 0
    else:
        resultado = numero ** potencia

    print(f'El resultado es: {resultado}')
    print(' ')
