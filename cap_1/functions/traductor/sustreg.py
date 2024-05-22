def sustreg(Ab, n):
    """
    Realiza el despeje para la matriz triangular superior aumentada
    Ab, que da solución al sistema Ax=b Donde A es de tamaño nxn y b de tamaño nx1
    """
    x = [0]*n
    x[n-1] = Ab[n-1][n] / Ab[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = 0
        for p in range(i+1, n):
            sum += Ab[i][p] * x[p]
        x[i] = (Ab[i][n] - sum) / Ab[i][i]
    return x
