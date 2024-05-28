import numpy as np


def Vandermonde(x, y):

    x = np.array([float(num) for num in x.strip("[]").split(" ")])
    y = np.array([float(num) for num in y.strip("[]").split(" ")])

    n = len(x)
    # Create the Vandermonde matrix
    A = np.vander(x, increasing=True)
    # Solve the system A * a = y to get the coefficients a
    a = np.linalg.solve(A, y)

    # Construct the polynomial as a string
    polynomial_terms = []
    for i in range(n):
        term = f"{a[i]:.6g}"
        if i > 0:
            term += " * " + " * ".join(["x" for j in range(i)])
        polynomial_terms.append(term)

    polynomial_str = " + ".join(polynomial_terms)
    print(polynomial_str)
    #img_interactiva = grafico_interactivo(function)

    mensaje = "it worked"

    return {'tabla': A,
            #'img_interactiva': img_interactiva,
            'funcion': polynomial_str,
            'mensaje': mensaje}


def ejemplo():
    # Example usage
    x = "[1 2 3 10 20]"
    y = "[2 3 5 -10 100]"

    resultados = Vandermonde(x, y)
    print(resultados['tabla'])


#ejemplo()
