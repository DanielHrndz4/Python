def titulo(titulo):
    titulo = parrafo.split()
    for palabra in titulo:
        print(palabra.capitalize(), end=' ')

parrafo = input('Digite su texto: ')
titulo(parrafo)