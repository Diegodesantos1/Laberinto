# El laberinto tiene una dimensión 5x5
muros = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
entrada= (0,0)
salida= (5,5)
def laberinto (dim,muros):
    laberinto = []
    # coordenada1= i
    # coordenada2= j
    for i in range(dim):
        fila = []
        for j in range(dim):
            if tuple ([i,j]) in entrada:
                fila.append('E')
            if tuple([i,j]) in salida:
                fila.append('S')
            if tuple([i,j]) in muros:
                fila.append('X')
            else:
                fila.append(' ')
        laberinto.append(fila)
    return laberinto

dibujolaberinto= laberinto(5,muros)

for i in dibujolaberinto:
    print(''.join(i))
