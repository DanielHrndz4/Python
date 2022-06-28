lenguajes = ('python', 'c++', 'java', 'php', 'php')
print(lenguajes)
# son de tama;o estatico
# lenguajes.remove('ruby')
print(lenguajes[0])
# lenguajes[0] = 'PYTHON' no se pueden modificar sus elementos

print(len(lenguajes))
for lenguaje in lenguajes:
    print(lenguaje)

print(lenguajes.count('php'))

del lenguajes
