u1 = {
    "id": 1,
    "usuario": "alicia",
    "correo": "alicia@gmail.com",
    "token": "dfhsdkjghsdkgffdhgfhdjgdjfghjkfdhgjf",
    "rol":{
        1: "admin",
        2: "gerente",
    }
}

u2 = {
    "id": 2,
    "usuario": "beto",
    "correo": "beto@gmail.com",
    "token": "rweiuyrewiurywetiowetyeweotoiewyttyew",
    "rol":{
        3: "ventas",
    }
}

lista_usuarios = [u1, u2]
# lista_usuarios.append(u1)
# lista_usuarios.append(u2)

print(lista_usuarios)
# dicci_alicia = lista_usuarios[0]
# print(dicci_alicia["usuario"])
# dicci_beto= lista_usuarios[1]
# print(dicci_beto["correo"])
print(lista_usuarios[0]["correo"])
print(lista_usuarios[0]["rol"][2])
for k,v in lista_usuarios[0]["rol"].items():
    print(k,v)