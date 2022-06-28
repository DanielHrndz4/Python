menu =  "***************MENU****************\n"
menu += "* 1. Agregar Empleado             *\n"          
menu += "* 2. Imprimir Lista               *\n"
menu += "* 3. Salir                        *\n"
menu += "***********************************"
print(menu)

lista = []

op = int(input("Digite la opcion: "))
while(op>=1 and op<=3):
    if op == 1:
        print("Digite el trabajador")
        nombre = input("Digite su nombre de usuario: ")
        cargo = input("Digite su cargo: ")
        sueldo = float(input("Digite su salario: "))
        print(" ")
        print("Trabajador guardado con exito...")
        d1 = {
        "usuario": nombre,
        "cargo": cargo,
        "sueldo": sueldo,
        }
        lista.append(d1) 
    elif op == 2:
        for diccionario in lista:
            print(diccionario)                     
    else:
        print ("Saliendo del programa...")
        exit()
    input()
    print(menu)
    op = int(input("Digite la opcion: "))