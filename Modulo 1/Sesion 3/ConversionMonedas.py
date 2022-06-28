inicio = 1

while inicio ==1:
    print("1. Colon A Dolar")
    print("2. Dolar a Bitcoin")
    print("3. Euro a Dolar")
    op = int(input("Digite la opcion: "))

    if op==1:
        cantidad = float(input("Digite la cantidad en colones: "))
        resultado = cantidad * 0.11
        print(cantidad,"Colones son",resultado,"Dolares")
    elif op==2:
        cantidad = float(input("Digite la cantidad en dolares: "))
        resultado = cantidad * 0.000016
        print(cantidad,"Dolares son",resultado,"Bitcoins")
    elif op==3:
        cantidad = float(input("Digite la cantidad en euros: "))
        resultado = cantidad * 1.16
        print(cantidad,"Euros son",resultado,"Dolares")
    else:
        print("Opcion no valida")
    print(" ")


