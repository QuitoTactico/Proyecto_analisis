from math import *
from .base import func as base_func, graficar_template

class iteracion:
    def __init__(self, i:int, x:float, fx:float, err:float):
        self.i = i
        self.x = x
        self.fx = fx
        self.err = err

    def __str__(self):
        return f'{self.i} | {self.x} | {self.fx} | {self.err}'

    def __repr__(self):
        return f'{self.i} | {self.x} | {self.fx} | {self.err}'


def biseccion_func(funcion:str, a:float, b:float, tol:float, niter:int):
    """
    Implementación método de bisección
    Entradas:
    funcion -- función
    a -- inicio intervalo
    b -- fin intervalo
    tol -- tolerancia
    niter -- número máximo de iteraciones
    """

    def func(x):
        return base_func(funcion, x)
    
    img = graficar_template(funcion)
    i = 1
    tabla = []

    while True:

        x = (b + a)/2

        x_menos_uno = float(tabla[-1].x) if i!=1 else None

        fx = func(x)

        err = abs(x - x_menos_uno) if x_menos_uno else None

        '''
        tabla.append({'i'   : i, 
                      'x'   : f'{x:.30f}', 
                      'fx'  : f'{fx:.30f}', 
                      'err' : f'{err:.30f}' if err else None})
        '''

        tabla.append(iteracion(i, 
                               f'{x:.30f}', 
                               f'{fx:.30f}', 
                               f'{err:.30f}' if err else None))
      
        # si f(x) = 0 o el error es menor que la tolerancia, terminamos
        err = err if err else 1 # para la comparación
        if abs(fx) <= 1e-64 or err <= tol:
            return {'sol'   : x, 
                    'iter'  : i, 
                    'tabla' : tabla, 
                    'img'   : img,
                    'final' : 'PUNTO ENCONTRADO'}
        # si se pasó de iteraciones, también, pero no se encontró el punto.
        elif i >= niter:
            return {'sol'   : x, 
                    'iter'  : i, 
                    'tabla' : tabla, 
                    'img'   : img,
                    'final' : 'ITERACIONES AGOTADAS'}
        # si no, seguimos
        else:
            if func(a)*fx > 0:
                a = x
            elif func(b)*fx > 0:
                b = x
            i += 1

'''
def test():
    # a = -2, b = 5, TOL = 1e-20, N0 = 100
    res = biseccion_func('2x-1', -2, 5, 1e-20, 100)

    for iteracion in res['tabla']:
        print(iteracion.i, iteracion.x, iteracion.fx, iteracion.err)

    print(res['final'])
    print(f'Solución: {res["sol"]}')
    print(f'Iteraciones: {res['iter']}')


test()
'''