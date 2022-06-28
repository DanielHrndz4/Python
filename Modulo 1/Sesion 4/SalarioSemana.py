nombre = input("Digite su nombre: ")
dui = int(input("Digite su numero de DUI: "))
horaTrabajada = int (input("Digite las horas trabajadas: "))
sueldo = 0
if horaTrabajada<=40:
    sueldo = horaTrabajada * 10
else:
    horaExtra = horaTrabajada - 40 
    sueldo = 400 + horaExtra * 20
print(" ")
print(f"Nombre: {nombre}\nDUI: {dui}\nSueldo: {sueldo}")
print("Datos guardados...")