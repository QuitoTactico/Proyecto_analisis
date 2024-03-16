from math import *

def funcion(x):
    """Función de prueba"""
    return x**2 + exp(-2*x) - 2*x*exp(-x)

def funcionprima(x):
    """Derivada función de prueba"""
    return 2*x - 2*exp(-2*x) - 2*exp(-x) + 2*x*exp(-x)

def newton(f, fprima, p0, tol, n):
    """
    Implementación método de Newton
    Entradas:
    f -- función
    fprima -- derivada función f
    p0 -- aproximación inicial
    tol -- tolerancia
    n -- número máximo de iteraciones

    Salida:
    p aproximación a cero de f
    None en caso de iteraciones agotadas
    """
    i = 1
    tabla = []

    while i <= n:
        p = p0 - f(p0)/fprima(p0)
        err = abs(p - p0)
        tabla.append({'i' : i, 'p' : f'{p:.30f}', 'f(p)' : f'{f(p):.30f}', 'err' : f'{err:.30f}'})
        
        if abs(f(p)) <= 1e-30 or err <= tol:
            return p, tabla, True

        p0 = p
        i += 1

    if i > n:
        print("Iteraciones agotadas: Error!")
        return p, tabla, False

    return None

# expo(x), expoprima(x), p0 = 4.0, TOL = 10^-8, N0 = 100
p, tabla, iter = newton(funcion, funcionprima, 4, 1e-8, 100)

for iteracion in tabla:
    print(iteracion)

iter_str = 'No agotadas' if iter else 'Iteraciones agotadas'
print(iter_str)