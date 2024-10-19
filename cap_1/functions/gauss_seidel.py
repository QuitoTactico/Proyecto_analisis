import numpy as np


class Iteracion:
    def __init__(self, c, error, x0):
        self.c = c
        self.error = error
        self.x0 = list(x0)

    def __str__(self):
        return f'{self.c} | {self.error} | {self.x0}'

    def __repr__(self):
        return f'{self.c} | {self.error} | {self.x0}'


def Gauss_seidel(x0, A, b, Tol, niter):

    # input error
    try:
        x0 = np.array([float(num) for num in x0.strip("[]").split(" ")])
        a = A.strip("[]").split(";")
        A = []
        for row in a:
            A.append([float(num) for num in row.split()])
        A = np.array(A)
        b = np.array([float(num) for num in b.strip("[]").split(" ")])
        Tol = float(Tol)
        niter = int(niter)
    except ValueError:
        return {'mensaje': "Incorrect format for input values. Ensure all inputs are correctly formatted."}

    # matrix shape error
    if A.shape[0] != A.shape[1]:
        return {'mensaje': "Matrix A must be square."}
    if len(x0) != A.shape[0]:
        return {'mensaje': "Initial guess vector x0 must be the same length as the dimensions of matrix A."}
    if len(b) != A.shape[0]:
        return {'mensaje': "Vector b must be the same length as the dimensions of matrix A."}

    c = 0
    error = Tol + 1
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    tabla = []

    # radius error
    T = np.linalg.inv(D) @ (L + U)
    spectral_radius = max(abs(np.linalg.eigvals(T)))
    if spectral_radius >= 1:
        return {'mensaje': "The matrix A is not suitable for the Jacobi method (spectral radius >= 1). The method may not converge."}

    while error > Tol and c < niter:
        T = np.linalg.inv(D - L) @ U
        C = np.linalg.inv(D - L) @ b
        x1 = T @ x0 + C
        error = np.linalg.norm(x1 - x0, np.inf)
        x0 = x1
        c += 1
        tabla.append(Iteracion(c,
                               error,
                               x0))

    if error < Tol:
        mensaje = 'PUNTO ENCONTRADO'
    else:
        mensaje = 'ITERACIONES AGOTADAS'

    return {'solucion': x0,
            'iteraciones': c,
            'tabla': tabla,
            'mensaje': mensaje}


def ejemplo():
    # Ejemplo de uso
    x0 = "[0 0 0]"  # Ejemplo de vector inicial
    A = "[4 -1 0; -1 4 -1; 0 -1 4]"  # Ejemplo de matriz A
    b = "[1 2 3]"  # Ejemplo de vector b
    Tol = "1e-5"
    niter = "100"

    iteraciones = Gauss_seidel(x0, A, b, Tol, niter)
    print(iteraciones['tabla'])


#ejemplo()
