nombres = ["alicia", "beto", "carlos", "diana"]
print(len(nombres))
print(nombres[3])
nombres[3] = "eva"

print(nombres)

nombres.append("fran")
print(nombres)

for nombre in nombres:
    print(nombre)

nombres.append("eva")
print(nombres)

nombres.remove('beto')
print(nombres)

nombres.insert(2, 'gabriela')
print(nombres)

nombres.sort()
print(nombres)

nombres.reverse()
print(nombres)

print('eva' in nombres)

nombres.clear()
print(nombres)

del nombres
# print(nombres)

numeros = [1,2,3,4]
print(min(numeros))

for numero in numeros:
    if numero < 2:
        print("menor")

lista =[n for n in numeros if n<3]
print(lista)
