class Empleado:
    def __init__(self, nombres):
        self.nombres = nombres
    def calcular_sueldo(self):
        """
        Empleado -> sueldo base
        Empleado por comision -> ventas * comision
        Empleado por hora -> valor * horas_trabajadas
        """
        return 1000

class EmpleadoPorComision(Empleado):
    def __init__(self,nombres,ventas,comision):
        super().__init__(nombres)
        self.ventas = ventas
        self.comision = comision
    def calcular_sueldo(self):
        return self.ventas * self.comision

class EmpleadoPorHora(Empleado):
    def __init__(self, nombres,horas,valor,he):
        super().__init__(nombres)
        self.horas = horas
        self.valor = valor
        self.he = he
    def calcular_sueldo(self):
        return self.horas * self.valor + self.he * self.he * self.valor * 2
