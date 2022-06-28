sueldo = float(input("Digite su sueldo: "))

if sueldo >= 1000.00:
    isss = 30.00
    afp = sueldo * 0.0725
    sueldo = sueldo - isss -afp
else: 
    isss = sueldo * 0.03
    afp = sueldo * 0.0725
    sueldo = sueldo - isss - afp
if sueldo > 0 and sueldo <= 472.00:
    print("Tramo 1")
    print("Sin retencion de impuestos")
elif sueldo >= 472.01 and sueldo <= 895.24:
    descuentoIsr = (sueldo - 472.00) * 0.1 + 17.67
    descuento = descuentoIsr + isss + afp
    sueldoNeto = sueldo - descuento
    print("Tramo 2")
    print("Descuento ISR", descuentoIsr)
    print("Total descuento: ", descuento)
    print("Sueldo neto: ", sueldoNeto)
elif sueldo >=895.25 and sueldo <=2038.10:
    descuentoIsr = (sueldo - 895.24) * 0.2 + 60.00
    descuento = descuentoIsr + isss + afp
    sueldoNeto = sueldo - descuento
    print("Tramo 3")
    print("Descuento ISR", descuentoIsr)
    print("Total descuento: ", descuento)
    print("Sueldo neto: ", sueldoNeto)
elif sueldo >=2038.11:
    descuentoIsr = (sueldo - 2038.10) * 0.3 + 288.57
    descuento = descuentoIsr + isss + afp
    sueldoNeto = sueldo - descuento
    print("Tramo 4")
    print("Descuento ISR", descuentoIsr)
    print("Total descuento: ", descuento)
    print("Sueldo neto: ", sueldoNeto)
else:
    print("Valor no definido")