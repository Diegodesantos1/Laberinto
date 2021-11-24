
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

def laberinto ():
    global dibujolaberinto
    dibujolaberinto = []
    coordenada1="i"
    coordenada2="j"
    for i in range:
        fila = []
    for j in range:
        if tuple([coordenada1, coordenada2]) in muro:
            fila.append('X')
        else:
            fila.append('  ')
        laberinto.append(fila)
    return laberinto
