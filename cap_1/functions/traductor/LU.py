import pivLu
import sustpro
import sustreg


def LU(A, b, n, Piv):
    """
    Calcula la solución de un sistema de ecuaciones Ax=b 
    mediante la factorización de A=LU ya sea sin pivoteo piv=0 
    o usando pivoteo parcial piv=1. Donde A es de tamaño nxn y b de tamaño nx1
    """
    P = [[0]*n for _ in range(n)]
    for i in range(n):
        P[i][i] = 1
    L = [[0]*n for _ in range(n)]
    for k in range(n-1):
        if Piv == 1:
            A, P = pivLu.pivLU(A, P, n, k)
        for i in range(k+1, n):
            M = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= M * A[k][j]
            A[i][k] = M
    U = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            U[i][j] = A[i][j]
    for i in range(n):
        for j in range(i):
            L[i][j] = A[i][j]
        L[i][i] = 1
    B = [0]*n
    for i in range(n):
        for j in range(n):
            B[i] += P[i][j] * b[j]
    LB = [L[i] + [B[i]] for i in range(n)]
    z = sustpro.sustpro(LB, n)
    Uz = [U[i] + [z[i]] for i in range(n)]
    x = sustreg.sustreg(Uz, n)
    print('x:', x, 'L:', L, 'U:', U)
    return x, L, U
LU([[4, 3, -2,-7], [3, 12, 8,-3], [2, 3, -9,3],[1, -2, -5, 6]], [20, 18, 31, 12], 4, 0)