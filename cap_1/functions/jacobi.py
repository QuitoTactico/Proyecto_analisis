import numpy as np


class Iteracion:
    def __init__(self, ite, err, sol):
        self.ite = ite
        self.err = err
        self.sol = sol

    def __str__(self):
        return f'{self.ite} | {self.err} | {self.sol}'

    def __repr__(self):
        return f'{self.ite} | {self.err} | {self.sol}'


def MatJacobi(x0, A, b, Tol, niter):
    c = 0
    error = Tol + 1
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)

    tabla = []

    while error > Tol and c < niter:
        T = np.linalg.inv(D) @ (L + U)
        C = np.linalg.inv(D) @ b
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
    x0 = np.array([0, 0, 0])  # Ejemplo de vector inicial
    A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]])  # Ejemplo de matriz A
    b = np.array([1, 2, 3])  # Ejemplo de vector b
    Tol = 1e-5
    niter = 100

    iteraciones = MatJacobi(x0, A, b, Tol, niter)
    print(iteraciones['tabla'])


ejemplo()
