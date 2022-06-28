from producto import Producto
from cliente import Cliente

class Factura:
    @staticmethod
    def n_factura(noFactura):
        noFactura = 1
    def __init__(self,idfactura, fecha, cliente):
        self.__idfactura = noFactura
        self.__fecha = fecha
        self.__cliente = Cliente
    def agregar_producto(self):
        self.lista_productos = list<Producto>()
    def __str__(self):
        return f'Lista: {self.lista_productos} | ID: {self.__idfactura} | Fecha: {self.__fecha} | Cliente: {self.__cliente}'
        