from math import *

def f(x):
    """Función de prueba"""
    return x**3 - 10*x**2 + 5

def busqueda_incremental(f, a, b, dx, n):
    """
    Implementación método de búsqueda incremental
    Entradas:
    f -- función
    a, b -- intervalo de búsqueda
    dx -- incremento

    Salida:
    x aproximación a cero de f
    None en caso de no encontrar cero en el intervalo
    """
    x0 = a
    f0 = f(a)
    tabla = []
    i = 1

    while x0 < b and i < n:
        x1 = x0 + dx
        f1 = f(x1)

        tabla.append({'i':i,'x0' : f'{x0:.25f}', 'x1' : f'{x1:.25f}', 'f(x0)' : f'{f0:.25f}', 'f(x1)' : f'{f1:.25f}'})
        if f0*f1 < 0:
            return (x0 + x1)/2, [x0,x1], tabla

        x0 = x1
        f0 = f1
        i +=1
    
    if i == n:
        print("Iteraciones agotadas: Error!")
        return None

    print("No se encontró cero en el intervalo.")
    return None

# f(x), a = 0, b = 1, dx = 0.2, n = 100
x, rango, tabla = busqueda_incremental(f, -3, 10, 0.2, 100)

for iteracion in tabla:
    print(iteracion)

if x is not None:
    print(f'x = {x:.30f}')

if rango is not None:
    print(f'Intervalo = {rango}')