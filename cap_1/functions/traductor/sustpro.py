def sustpro(Ab, n):
    """
    Realiza el despeje para la matriz triangular inferior aumentada
    Ab, que da solución al sistema Ax=b Donde A es de tamaño nxn y b de tamaño nx1
    """
    x = [0]*n
    x[0] = Ab[0][n] / Ab[0][0]
    for i in range(1, n):
        sum = 0
        for p in range(i):
            sum += Ab[i][p] * x[p]
        x[i] = (Ab[i][n] - sum) / Ab[i][i]
    return x