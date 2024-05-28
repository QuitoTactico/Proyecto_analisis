import numpy as np
from base import func as base_func, grafico_interactivo
from bokeh.plotting import show


def NewtonInt(x: np.array.__class__, y: np.array.__call__):
    n = len(x)
    Tabla = np.zeros((n, n + 1))
    Tabla[:, 0] = x
    Tabla[:, 1] = y

    for j in range(2, n + 1):
        for i in range(j - 1, n):
            Tabla[i, j] = (Tabla[i, j - 1] - Tabla[i - 1, j - 1]) / (Tabla[i, 0] - Tabla[i - (j - 1), 0])

    mensaje = "it worked"

    coefficients = Tabla[np.arange(n), np.arange(1, n + 1)]

    # Constructing the polynomial as a string
    polynomial_terms = []
    for i in range(n):
        term = f"{coefficients[i]:.6g}"
        for j in range(i):
            term += f" * (x - {x[j]:.6g})"
        polynomial_terms.append(term)

    polynomial_str = " + ".join(polynomial_terms)
    print(polynomial_str)

    #img_interactiva = grafico_interactivo(function)

    return {'tabla': Tabla,
            #'img_interactiva': img_interactiva,
            'funcion': polynomial_str,
            'mensaje': mensaje}


def ejemplo():
    # Ejemplo de uso
    x = np.array([1, 4, 13, 20])  # Ejemplo de puntos x
    y = np.array([-10, 8, -20, 1])  # Ejemplo de puntos y

    resultado = NewtonInt(x, y)
    print("Tabla de diferencias divididas de Newton:")
    print(resultado['tabla'])


ejemplo()
