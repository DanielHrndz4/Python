menu = "*************** MENU ******************\n"
menu += "1. Bitcoin a Dolar\n"
menu += "2. Dolar a Bitcoin\n"
menu += "#. Salir\n"
menu += "****************************************\n"

print(menu)
op = int(input("Seleccione una opcion: "))
while(op>=1 and op <=2):
    cantidad = float(input("digite la cantidad: "))
    if op==1:
        resultado = cantidad * 60000
    else:
        resultado = cantidad / 60000
    print(f"La conversion es: {resultado:.2f}")
    
    input()
    print(menu)
    op = int(input("Seleccione una opcion: "))
