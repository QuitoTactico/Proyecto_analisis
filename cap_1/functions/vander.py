import numpy as np
from .base import func as base_func, graficar_template, grafico_interactivo
from bokeh.plotting import show


def Vandermonde(x, y):

    # input error
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

    # algebra error
    try:
        # Create the Vandermonde matrix
        A = np.vander(x, increasing=True)
        # Solve the system A * a = y to get the coefficients a
        a = np.linalg.solve(A, y)
    except np.linalg.LinAlgError as e:
        return {'mensaje': f"Linear algebra error: {e}"}

    # Construct the polynomial as a string
    polynomial_terms = []
    for i in range(n):
        term = f"{a[i]:.6g}"
        if i > 0:
            term += " * " + " * ".join(["x" for _ in range(i)])
        polynomial_terms.append(term)

    polynomial_str = " + ".join(polynomial_terms)

    img_interactiva = grafico_interactivo(polynomial_str,
                                          a=x[0],
                                          b=x[-1],
                                          puntos=zip(x, y))

    return {'tabla': A,
            'img_interactiva': img_interactiva,
            'funcion': polynomial_str,
            'mensaje': "it worked"}


def ejemplo():
    # Example usage
    x = "[1 2 3 10 20]"
    y = "[2 3 5 -10 100]"

    resultados = Vandermonde(x, y)
    print(resultados['tabla'])
    #show(resultados['img_interactiva'])


#ejemplo()
