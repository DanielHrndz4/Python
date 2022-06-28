from figura import Figura

class Circulo(Figura):
    def __init__(self,inicio,pi,r):
        super().__init__(inicio)
        self.pi = pi
        self.r = r
        
    def calcular_area(self):
        return (self.pi*self.r)**2
    def calcular_perimetro(self):
        return 2*self.pi*self.r 

r2 = Circulo('Inicio',3.1416,2)
r2.mostrar_inicio()
print(f'Area: {r2.calcular_area()}')
print(f'Perimetro: {r2.calcular_perimetro()}')
