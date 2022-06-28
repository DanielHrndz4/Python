from empleado import Empleado, EmpleadoPorComision, EmpleadoPorHora

e1 = Empleado('Daniel')
e2 = EmpleadoPorComision('Jonathan', 2000.0, 0.3)
e3 = EmpleadoPorHora('Katherine', 200.0,7,10)

if isinstance(e3, object):
    print ('E3 es de tipo Object')

elif isinstance(e3, Empleado):
    print('E3 es un tipo Empleado')

elif isinstance(e3, EmpleadoPorHora):
    print('E3 es un tipo Empleado por hora')
