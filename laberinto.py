# El laberinto tiene una dimensión 6x6 para dejar más claro el dibujo del laberinto
muros = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3),(4, 0), (4, 1), (4, 2), (4, 3), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5))
entrada = ((0, 0), (0, 0))  # Lo pongo en forma de tupla
salida = ((4, 4), (4, 4))  # Lo pongo en forma de tupla


def laberinto(dim, muros):
    laberinto = []  # Creo una lista vacía para las filas
    # coordenada1= i
    # coordenada2= j
    for i in range(dim):
        fila = []  # Creo una lista vacía para las filas
        for j in range(dim):
            if tuple([i, j]) in muros:
                # Dejo 1 espacio para que sea más visual el laberinto
                fila.append("X ")
            elif tuple([i, j]) in entrada:
                fila.append("E ")  # Añado la entrada
            elif tuple([i, j]) in salida:
                fila.append("S ")  # Añado la salida
            else:
                # Dejo 2 espacios para que sea más visual el laberinto
                fila.append("  ")
        laberinto.append(fila)
    return laberinto


# Le pongo 6, ya que es la dimensión del laberinto
dibujolaberinto = laberinto(6, muros)

for i in dibujolaberinto:
    # Con esto convierto la lista en una cadena formada por los elementos de la lista separados por comas.
    print("".join(i))

# Parte 2 del código


def solucion_laberinto(laberinto):
    n = 6  # Dimensión del laberinto
    fila = columna = 0  # Empezamos por el 0,0
    # Desde la entrada empezamos hacia abajo para llegar a la salida según la imagen
    movimiento = ["Abajo"]
    while (fila < n - 1 and columna < n - 1):
        # Especifico que haga esto cuando no haya muro
        if movimiento[-1] != "Arriba" and fila + 1 < n and laberinto[fila + 1][columna] != "X ":
            fila += 1
            movimiento.append("Abajo")
        # Especifico que haga esto cuando no haya muro
        elif movimiento[-1] != "Abajo" and fila - 1 > 0 and laberinto[fila - 1][columna] != "X ":
            fila -= 1
            movimiento.append("Arriba")
        # Especifico que haga esto cuando no haya muro
        elif movimiento[-1] != "Derecha" and columna - 1 > 0 and laberinto[fila][columna - 1] != "X ":
            columna -= 1
            movimiento.append("Izquierda")
        # Especifico que haga esto cuando no haya muro
        elif movimiento[-1] != "Izquierda" and columna + 1 < n and laberinto[fila][columna + 1] != "X ":
            columna += 1
            movimiento.append("Derecha")
        else:
            # Establezco un caso en el que no haya salida, aunque en el laberinto dado, no es necesario
            movimiento.append("Sin salida")
    return movimiento


print(
    f"La solución para escapar del laberinto es la siguiente secuencia de movimientos {solucion_laberinto(dibujolaberinto)}")
