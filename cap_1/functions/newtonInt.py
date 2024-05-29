import numpy as np
#from base import func as base_func, grafico_interactivo
from .base import func as base_func, graficar_template, grafico_interactivo
from bokeh.plotting import show


def NewtonInt(x, y):
 
    try:
        x = np.array([float(num) for num in x.strip("[]").split()])
        y = np.array([float(num) for num in y.strip("[]").split()])
    except ValueError as e:
        return {'mensaje': f"Input parsing error: {e}"}

    n = len(x)
    if n != len(y):
        return {'mensaje': "Input vectors x and y must have the same length"}

    if n < 2:
        return {'mensaje': "At least two data points are required for interpolation"}

    if not np.all(np.diff(x) > 0):
        return {'mensaje': "Input x-values must be sorted in increasing order"}

    Tabla = np.zeros((n, n + 1))
    Tabla[:, 0] = x
    Tabla[:, 1] = y

    for j in range(2, n + 1):
        for i in range(j - 1, n):
            try:
                denominator = Tabla[i, 0] - Tabla[i - (j - 1), 0]
                if denominator == 0:
                    raise ZeroDivisionError("Division by zero")
                Tabla[i, j] = (Tabla[i, j - 1] - Tabla[i - 1, j - 1]) / denominator
            except ZeroDivisionError as e:
                return {'mensaje': f"Error in calculating divided difference at index ({i}, {j}): {e}"}

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
            'mensaje': "it worked"}


def ejemplo():
    # Ejemplo de uso
    x = "[1 4 13 20]"  # Ejemplo de puntos x
    y = "[-10 8 -20 1]"  # Ejemplo de puntos y

    resultado = NewtonInt(x, y)
    print("Tabla de diferencias divididas de Newton:")
    print(resultado['tabla'])


#ejemplo()
