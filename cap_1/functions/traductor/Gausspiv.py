import numpy as np
import pivpar
import pivtot
import sustreg

def GaussPiv(A, b, n, Piv):
    """
    Calcula la solución de un sistema de ecuaciones Ax=b, ya sea
    sin pivoteo piv=0, usando pivoteo parcial piv=1 o pivoteo total piv=2. 
    Donde A es de tamaño nxn y b de tamaño nx1
    """
    Ab = [A[i] + [b[i]] for i in range(n)]
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
    A = np.array(A)
    x_ordered = np.array(x_ordered)
    b = np.array(b)

    # Calculate the error vector
    error_vector = np.abs(np.dot(A, x_ordered) - b)
    print('Error vector:', [format(e, '.30f') for e in error_vector])

    # Calculate the error scalar
    error_scalar = np.linalg.norm(np.dot(A, x_ordered) - b)
    print('Error scalar:', format(error_scalar, '.30f'))

    print('x:', [format(e, '.30f') for e in x_ordered], 'mark:', mark)
    return x_ordered, mark, error_vector, error_scalar

GaussPiv([[5.4, -3.2, 8.1], [17, 21, -22], [3, -4, 4]], [13, 25, -8], 3, 2)