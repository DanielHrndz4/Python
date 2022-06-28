from figura import Figura

class Rectangulo(Figura):

    def __init__(self,inicio,base,altura):
        super().__init__(inicio)
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return (self.base + self.altura) * 2

r1 = Rectangulo('Inicio',20,30)
r1.mostrar_inicio()
print(f'Area: {r1.calcular_area()}')
print(f'Perimetro: {r1.calcular_perimetro()}')
