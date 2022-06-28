inicio = True
while(inicio == True):
    def validarInt(numero):
        n = None #None = False
        try:
            n = int(numero)
            return n
        except Exception as e:
            print(e)
            return n

    op = input('Digite el numero: ')
    if validarInt(op):
        print('La opcion es entera')
    else:
        print('La opcion no es entera')
input()

