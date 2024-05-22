from decimal import Decimal, getcontext
import pivpar
import pivtot
import sustreg

getcontext().prec = 20  # Set the precision to 50

def GaussPiv(A, b, n, Piv):
    """
    Calcula la solución de un sistema de ecuaciones Ax=b, ya sea
    sin pivoteo piv=0, usando pivoteo parcial piv=1 o pivoteo total piv=2. 
    Donde A es de tamaño nxn y b de tamaño nx1
    """
    Ab = [[Decimal(a_ij) for a_ij in A[i]] + [Decimal(b[i])] for i in range(n)]
    mark = list(range(n))
    for k in range(n-1):
        if Piv == 1:
            Ab = pivpar.pivpar(Ab, n, k)
        elif Piv == 2:
            Ab, mark = pivtot.pivtot(Ab, mark, n, k)
        for i in range(k+1, n):
            M = Ab[i][k] / Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] -= M * Ab[k][j]
    x = sustreg.sustreg(Ab, n)

    # Order x according to mark
    x_mark_pairs = list(zip(x, mark))
    x_mark_pairs.sort(key=lambda pair: pair[1])
    x_ordered = [pair[0] for pair in x_mark_pairs]

    # Convert A, x_ordered, and b to numpy arrays for matrix operations
    A = [[Decimal(a_ij) for a_ij in row] for row in A]
    x_ordered = [Decimal(x_i) for x_i in x_ordered]
    b = [Decimal(b_i) for b_i in b]

    # Calculate the error vector
    error_vector = [abs(A[i][j]*x_ordered[j] - b[i]) for i in range(n) for j in range(n)]
    print('Error vector:', [str(e) for e in error_vector])

    # Calculate the error scalar
    error_scalar = sum(e**2 for e in error_vector).sqrt()
    print('Error scalar:', str(error_scalar))

    print('x:', [str(e) for e in x_ordered], 'mark:', mark)
    return x_ordered, mark, error_vector, error_scalar

GaussPiv([[5.4, -3.2, 8.1], [17, 21, -22], [3, -4, 4]], [13, 25, -8], 3, 2)