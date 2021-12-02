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

def solucion_laberinto():
    n = 5 #Dimensión del laberinto
    fila = columna = 0 #EMpezamos por el 0,0
    movimiento= ["Abajo"]
    while fila < n - 1 and columna < n-1:
        if movimiento [-1] != "Arriba" and fila + 1 < n:
            fila += 1
            movimiento.append ("Abajo")
        elif movimiento [-1] != "Abajo" and fila - 1 > 0:
            fila -= 1
            movimiento.append("Arriba")
        elif movimiento [-1] != "Derecha" and columna - 1 < 0:
            columna -= 1
            movimiento.append("Izquierda")
        elif movimiento [-1] != "Izquierda" and columna + 1 < n:
            columna -= 1
            movimiento.append("Izquierda")
        else:
            movimiento.append("Sin salida")
    return movimiento
solucion_laberinto()
print(solucion_laberinto)

