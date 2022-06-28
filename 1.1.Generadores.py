#GENERADOR YIELD
def generaPares(limite):
    limite = int(input("Digita un numero: "))
    num=1
    while (num<limite):
        yield num*2
        num=num+1
devuelvePares=generaPares(limite)
for i in devuelvePares:
    print(i)
