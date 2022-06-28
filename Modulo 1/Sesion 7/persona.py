class Persona:
    def __init__(self, nombres, apellidos, edad, dui):
        self.nombres = nombres #PUBLICO
        self._apellidos = apellidos #PROTEGIDO
        self.__edad = edad #PRIVADO
        self.__dui = dui #PRIVADO
    def mostrar_datos(self):
        print(f'Nombre: {self.nombres}\n'
              f'Apellidos: {self._apellidos}\n'
              f'Edad: {self.__edad}\n'
              f'DUI: {self.__dui}')
    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
        self.__edad = edad
    def get_dui(self):
        return self.__dui
    def __str__(self):
        return f'{self.nombres} | {self._apellidos} | {self.__edad} | {self.__dui}'

p = Persona('Daniel', 'Hernandez', 19, '063978123')
# print(p)
# print('El nombre es:', p.nombres)
# print('El apellido es:',p._apellidos)
# # print(f'La edad es:', p.__edad) ATRIBUTOS PRIVADOS
# # print(f'El numero de DUI es:', p.__dui) ATRIBUTOS PRIVADOS
# print('La edad es:',p.get_edad())
# print('Numero de DUI:',p.get_dui())
p.mostrar_datos()
print(p)
print('**********************************************')
p_beto = Persona('Beto', 'Joel', 30, '12478569')
p_beto.mostrar_datos()
print(p_beto)