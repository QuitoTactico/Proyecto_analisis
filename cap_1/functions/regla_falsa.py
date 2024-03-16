from math import *

def funcion(x):
    """Función de prueba"""
    return exp(x) + 3*cos(x)

def bisec(f, a, b, tol, n):
    """
    Implementación método de bisección
    Entradas:
    f -- función
    a -- inicio intervalo
    b -- fin intervalo
    tol -- tolerancia
    n -- número máximo de iteraciones

    Salida:
    p aproximación a cero de f
    None en caso de iteraciones agotadas
    """
    i = 1

    tabla = []

    while i <= n:
        p = a-(f(a)*(b-a))/(f(b)-f(a))
        err = abs(p- float(tabla[-2]['p']) if len(tabla) > 1 else 1)
        tabla.append({'i' : i, 'p' : f'{p:.30f}', 'f(p)' : f'{f(p):.30f}', 'err' : f'{err:.30f}'})
        if abs(f(p)) <= 1e-30 or err <= tol:
            return p, tabla, True
        i += 1
        if f(a)*f(p) > 0:
            a = p
        else:
            b = p
    if i > n:
        print("Iteraciones agotadas: Error!")
        return p, tabla, False
    return None

# a = 1, b = 2, T OL = 10−8, N0 = 100
p, tabla, iter = bisec(funcion, -2, -1.5, 1e-20, 100)

for iteracion in tabla:
    print(iteracion)

iter_str = 'No agotadas' if iter else 'Iteraciones agotadas'
print(iter_str)