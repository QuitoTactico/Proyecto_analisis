def pivtot(Ab, mark, n, k):
    """
    Realiza el pivoteo total(por filas y columnas) sobre la matriz aumentada AB del
    sistema Ax=b
    """
    mayor = 0
    maxrow = k
    maxcol = k
    for r in range(k, n):
        for s in range(k, n):
            if abs(Ab[r][s]) > mayor:
                mayor = abs(Ab[r][s])
                maxrow = r
                maxcol = s
    if mayor == 0:
        print('El sistema no tiene solución única')
    else:
        if maxrow != k:  # intercambio de filas
            Ab[k], Ab[maxrow] = Ab[maxrow], Ab[k]
        if maxcol != k:  # intercambio de columnas
            for i in range(n):
                Ab[i][k], Ab[i][maxcol] = Ab[i][maxcol], Ab[i][k]
            mark[k], mark[maxcol] = mark[maxcol], mark[k]
    return Ab, mark