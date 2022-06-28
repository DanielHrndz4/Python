nombres = {"alicia", "beto", "carlos", "diana",1}

print(nombres)
# no es posible el acceso indexado
# print(nombres[0])

for otra_cosa in nombres:
    print(otra_cosa)

nombres.add("eva")
print(nombres)

nombres.add("eva") # no acepta duplicados
print(nombres)

# no permite modificar un elemento
# nombres[0] = "fran"

nombres.discard("Eva".lower())
print(nombres)

nombres.clear()
print(nombres)

del nombres
# eliminar repetidos
lista = [1,2,3,3,3]
conjunto = set(lista)
print(conjunto)