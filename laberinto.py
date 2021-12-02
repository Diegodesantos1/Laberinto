# El laberinto tiene una dimensión 5x5
muros = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
entrada= (0,0)
salida= (5,5)
def laberinto (dim,muros):
    laberinto = [] #Creo una lista vacía para las filas
    # coordenada1= i
    # coordenada2= j
    for i in range(dim):
        fila = [] #Creo una lista vacía para las filas
        for j in range(dim):
            if tuple([i,j]) in muros:
                fila.append('X')
            else:
                fila.append(' ')
        laberinto.append(fila)
    return laberinto

dibujolaberinto= laberinto(5,muros) #Le pongo 5, ya que es la dimensión del laberinto

for i in dibujolaberinto:
    print(''.join(i)) #Con esto convierto la lista en una cadena formada por los elementos de la lista separados por comas.

#Parte 2 del código
