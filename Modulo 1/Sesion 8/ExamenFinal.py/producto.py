class Producto:
    def __init__(self,nombre_producto, precio, cantidad):
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.cantidad = cantidad
    def set_precio(self,precio):
        return self.precio
    def set_cantidad(self,cantidad):
        return self.cantidad
    def __str__(self):
        return f'Producto: {self.nombre_producto} | Cantidad: {self.cantidad}'