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


def SOR(x0, A, b, Tol, niter, w):
    c = 0
    error = Tol + 1
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    tabla = []

    while error > Tol and c < niter:
        T = np.linalg.inv(D - w * L) @ ((1 - w) * D + w * U)
        C = w * np.linalg.inv(D - w * L) @ b
        x1 = T @ x0 + C
        error = np.linalg.norm(x1 - x0, np.inf)
        x0 = x1
        c += 1
        tabla.append(Iteracion(c,
                               error,
                               x0))

    if error < Tol:
        print(f'es una aproximación de la solución del sistema con una tolerancia= {Tol}')
    else:
        print(f'Fracasó en {niter} iteraciones')

    return tabla


def ejemplo():
    # Ejemplo de uso
    x0 = np.array([0, 0, 0])  # Ejemplo de vector inicial
    A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]])  # Ejemplo de matriz A
    b = np.array([1, 2, 3])  # Ejemplo de vector b
    Tol = 1e-5
    niter = 100
    w = 1.25

    tabla = SOR(x0, A, b, Tol, niter, w)
    print(tabla)


ejemplo()
