# un diccionario cada elemento es un apar llave:valor
# nombre:alicia
diccionario = {
    "usuario": "alicia",
    "correo": "alicia@gmail.com",
    "token": "dfhsdkjghsdkgffdhgfhdjgdjfghjkfdhgjf",
}

print(diccionario)
# print(diccionario["usuario"])
# print(diccionario["correo"])
# print(diccionario["token"])

# for valor in diccionario.values():
#     print(valor)

# for clave in diccionario.keys():
#     print(clave)

diccionario["usuario"] = 'alicia.diaz'
diccionario["telefono"] = '77777777'
for clave, valor in diccionario.items():
    print(f'la clave es: {clave}, valor: {valor}')

print('usuario' in diccionario)
diccionario.clear()
print(diccionario)
del diccionario
print("hola 'mundo'", 'Hola "mundo"', 'hola \'mundo\'')
