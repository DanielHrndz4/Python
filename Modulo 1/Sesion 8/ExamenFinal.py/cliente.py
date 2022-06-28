class Cliente:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    def __str__(self):
        return f'Nombre: {self.__nombre} | Edad: {self.__edad}'