def pivpar(Ab, n, k):
    """
    Realiza el pivoteo parcial (por filas) sobre la matriz aumentada AB del
    sistema Ax=b
    """
    mayor = abs(Ab[k][k])
    maxrow = k
    for s in range(k+1, n):
        if abs(Ab[s][k]) > mayor:
            mayor = abs(Ab[s][k])
            maxrow = s
    if mayor == 0:
        print('El sistema no tiene solución única')
    elif maxrow != k:  # intercambio de filas
        Ab[k], Ab[maxrow] = Ab[maxrow], Ab[k]
    return Ab