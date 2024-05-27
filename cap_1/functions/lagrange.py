import numpy as np
from base import func as base_func, func_deriv as base_func_deriv, graficar_template, grafico_interactivo
from bokeh.plotting import show


def Lagrange(x, y):
    n = len(x)
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
                term_str += f"(x - {x[j]})"
        coef = y[i] / den
        term_str = f"{coef:.6g} * " + term_str
        polynomial_terms.append(term_str)
        Tabla[i, :] = y[i] * Li / den

    pol = np.sum(Tabla, axis=0)
    polynomial_str = " + ".join(polynomial_terms)
    print(polynomial_str)
    #img_interactiva = grafico_interactivo(function)
    mensaje = "se logro"

    return {'tabla': pol,
            #'img_interactiva': img_interactiva,
            'mensaje': mensaje}


def ejemplo():
    # Ejemplo de uso
    x = np.array([1, 2, 3, 10])
    y = np.array([2, 3, 5, -10])

    pol = Lagrange(x, y)
    print("Coeficientes del polinomio de interpolación de Lagrange:")
    print(pol['tabla'])


ejemplo()
