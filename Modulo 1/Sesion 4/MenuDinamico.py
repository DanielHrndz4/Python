menu = "***************MENU***************\n"
menu += "1. Bictcoin a Dolar\n"
menu += "2. Dolar a Bictcoin\n"
menu += "3. Salir\n"
menu += "**********************************"
print (menu)
op = int(input("Seleccione la opcion: "))
while(op>=1 and op<=2):
    cantidad = float(input("Digite la cantidad: "))
    if op==1:
        resultado = cantidad * 60000
    elif op==2:
        resultado = cantidad / 60000
    print(f"La conversion es: {resultado:.2f}")
    
    input()
    print(menu)
    
    op = int(input("Seleccione la opcion: "))
