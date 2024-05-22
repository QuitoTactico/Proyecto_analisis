def pivLU(A, P, n, k):
    """
    Realiza el pivoteo parcial (por filas) sobre la matriz A del
    sistema Ax=b para la factorización LU
    """
    mayor = abs(A[k][k])
    maxrow = k
    for s in range(k+1, n):
        if abs(A[s][k]) > mayor:
            mayor = abs(A[s][k])
            maxrow = s
    if mayor == 0:
        print('El sistema no tiene solución única')
    elif maxrow != k:  # intercambio de filas
        A[k], A[maxrow] = A[maxrow], A[k]
        P[k], P[maxrow] = P[maxrow], P[k]
    return A, P