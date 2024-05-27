import numpy as np


def Vandermonde(x, y):
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
            term += " * " + " * ".join([f"(x - {x[j]:.6g})" for j in range(i)])
        polynomial_terms.append(term)

    polynomial_str = " + ".join(polynomial_terms)
    return a, polynomial_str


def ejemplo():
    # Example usage
    x = np.array([1, 2, 3, 10])
    y = np.array([2, 3, 5, -10])

    coefficients, polynomial_str = Vandermonde(x, y)
    print("Coeficientes del polinomio de interpolación de Vandermonde:")
    print(coefficients)
    print("Polinomio de interpolación de Vandermonde:")
    print(polynomial_str)


ejemplo()
