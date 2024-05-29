import numpy as np
from .base import func as base_func, graficar_template, grafico_interactivo
from bokeh.plotting import show


def Lagrange(x, y):

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

    Tabla = np.zeros((n, n))
    polynomial_terms = []

    for i in range(n):
        Li = np.array([1])
        den = 1
        term_str = ""
        for j in range(n):
            if j != i:
                paux = np.array([1, -x[j]])
                Li = np.convolve(Li, paux)
                den *= (x[i] - x[j])
                term_str += f"(x-{x[j]})"
        coef = y[i] / den
        term_str = f"{coef:.6g}*" + term_str
        polynomial_terms.append(term_str)
        Tabla[i, :] = y[i] * Li / den

    pol = np.sum(Tabla, axis=0)
    polynomial_str = "+".join(polynomial_terms)

    print(polynomial_str)
    img_interactiva = grafico_interactivo(polynomial_str,
                                          a=x[0],
                                          b=x[-1],
                                          puntos=zip(x, y))

    return {'tabla': pol,
            'img_interactiva': img_interactiva,
            'funcion': polynomial_str,
            'mensaje': "it worked"}


def ejemplo():
    # Ejemplo de uso
    x = "[1 2 3 10]"
    y = "[2 3 5 -10]"

    pol = Lagrange(x, y)
    print("Coeficientes del polinomio de interpolación de Lagrange:")
    print(pol['tabla'])
    show(pol['img_interactiva'])


#ejemplo()
