from math import *

def funcion(x):
    """Función de prueba"""
    return exp(-x/4)

def puntofijo(f, p0, tol, n):
    """
    Implementación método de punto fijo
    Entradas:
    f -- función
    p0 -- aproximación inicial
    tol -- tolerancia
    n -- número máximo de iteraciones

    Salida:
    p aproximación a punto fijo de f
    None en caso de iteraciones agotadas
    """
    i = 1
    tabla = []

    while i <= n:
        p = f(p0)
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

# pol(x), p0 = 0.9, TOL = 10^-8, N0 = 100
p, tabla, iter = puntofijo(funcion, 0.9, 1e-8, 100)

for iteracion in tabla:
    print(iteracion)

iter_str = 'No agotadas' if iter else 'Iteraciones agotadas'
print(iter_str)
