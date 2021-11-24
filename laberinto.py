# El laberinto tiene una dimensión 5x5
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
dim=5
def laberinto (dim,muros):
    laberinto = []
    coordenada1="i"
    coordenada2="j"
    for i in range(dim):
        fila = []
        for j in range(dim):
            if tuple([coordenada1, coordenada2]) in muro:
                fila.append('X')
            else:
                fila.append('  ')
        laberinto.append(fila)
    return laberinto
