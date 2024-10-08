from math import *
from .base import func as base_func, grafico_interactivo
from bokeh.plotting import show


class Iteracion:
    def __init__(self, i: int, x: float, fx: float, err: float):
        self.i = i
        self.x = x
        self.fx = fx
        self.err = err

    def __str__(self):
        return f'{self.i} | {self.x} | {self.fx} | {self.err}'

    def __repr__(self):
        return f'{self.i} | {self.x} | {self.fx} | {self.err}'


def secante_func(funcion: str, x0: float, x1: float, error_type: str, tol: float, niter: int):
    """
    Implementación método de la secante
    Entradas:
    funcion -- función
    x0 -- aproximación inicial
    x1 -- segunda aproximación inicial
    tol -- tolerancia
    niter -- número máximo de iteraciones
    """

    haveFunc = True

    def func(x):
        return base_func(funcion, x)

    i = 2
    err, mensaje = 1, None
    tabla = []

    try:
        tabla.append(Iteracion(0,
                                f'{x0}',
                                f'{func(x0)}',
                                f'{1}'))
    except:
        haveFunc = False

    try:
        tabla.append(Iteracion(1,
                                f'{x1}',
                                f'{func(x1)}',
                                f'{abs(x1 - x0)}'))
    except:
        haveFunc = False

    if haveFunc:
        while True:
            # x = x actual = Xn+1
            # x1 = x anterior = Xn
            # x0 = x penúltimo = Xn-1

            if (func(x1) - func(x0)) == 0:
                mensaje = 'f(Xn) - f(Xn-1) = 0 (División por cero)'
                x = None
                break

            x = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))

            fx = func(x)

            if error_type == 'Error absoluto':
                err = abs(x - x1)
            elif error_type == 'Error relativo':
                err = abs((x - x1)/x)

            tabla.append(Iteracion(i, 
                                f'{x}', 
                                f'{fx}', 
                                f'{err}'))

            if abs(fx) <= 1e-64 or err <= tol:
                mensaje = 'PUNTO ENCONTRADO'
                break

            elif i >= niter:
                mensaje = 'ITERACIONES AGOTADAS'
                break

            else:
                x0 = x1
                x1 = x
                i += 1

    if haveFunc:
        a = min(float(iteracion.x) for iteracion in tabla)
        b = max(float(iteracion.x) for iteracion in tabla)
        img_interactiva = grafico_interactivo(funcion, metodo='secante', sol=x, a=a, b=b, vlines= [('x0', x0), ('x1', x1)])
    else:
        x, i, img_interactiva, mensaje = 0, 0, 0, 'FUNCTION WRITEN WRONG'

    return {'solucion': x,
            'iteraciones': i,
            'tabla': tabla,
            'img_interactiva': img_interactiva,
            'mensaje': mensaje}


def secante_test():
    res = secante_func(funcion='(x^3)-10x-5', x0=3, x1=2, error_type='Error absoluto', tol=1e-10, niter=100)

    for iteracion in res['tabla']:
        print(iteracion)

    print(res['mensaje'])
    print(f'Solución: {res["solucion"]}')
    print(f'Iteraciones: {res["iteraciones"]}')

    #show(res['img_interactiva'])
    #puntos = [(3, 0), (2, 0)]
    #show(grafico_interactivo('2x-3', a=3, b=5, puntos=puntos))

#secante_test()
