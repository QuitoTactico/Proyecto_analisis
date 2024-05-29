from math import *
from .base import func as base_func, graficar_template, grafico_interactivo
from bokeh.plotting import show


class Iteracion:
    def __init__(self, i:int, x:float, fx:float, err:float):
        self.i = i
        self.x = x
        self.fx = fx
        self.err = err

    def __str__(self):
        return f'{self.i} | {self.x} | {self.fx} | {self.err}'

    def __repr__(self):
        return f'{self.i} | {self.x} | {self.fx} | {self.err}'


def puntofijo_func(funcion: str, funcion_g: str, x0: float, error_type: str, tol: float, niter: int):
    """
    Implementación método de punto fijo
    Entradas:
    funcion -- función
    x0 -- aproximación inicial
    tol -- tolerancia
    niter -- número máximo de iteraciones
    """

    haveFunc = True

    def func(x):
        return base_func(funcion_g, x)

    i = 1
    x_anterior, err, mensaje = None, 1, None
    tabla = []
    x0_inicial = x0

    try:
        tabla.append(Iteracion(0,
                                f'{x0}',
                                f'{func(x0)}',
                                1))
    except:
        haveFunc = False

    if haveFunc:
        while True:
            x = func(x0)
            fx = func(x)

            x_anterior = float(tabla[-1].x)
            try:
                if error_type == 'Error absoluto':
                    err = abs(x - x_anterior)
                elif error_type == 'Error relativo':
                    err = abs((x - x_anterior)/x)
            except:
                x, i, img_interactiva, mensaje = 0, 0, 0, 'OVERFLOW'
                break

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
                x0 = x
                i += 1

        a = min(float(iteracion.x) for iteracion in tabla)
        b = max(float(iteracion.x) for iteracion in tabla)
        try:
            img_interactiva = grafico_interactivo(funcion,
                                                  metodo='puntofijo',
                                                  sol=x,
                                                  a=a,
                                                  b=b,
                                                  vlines=[('x0', x0_inicial)],
                                                  funcion_g=funcion_g)
        except:
            x, i, img_interactiva, mensaje = 0, 0, 0, 'FUNCION 1 MAL ESCRITA'
        # img_interactiva = grafico_interactivo(funcion, sol=x, a=a, b=b, vlines= [('x0', x0_inicial)], funcion_g='NEWTON')
    else:
        x, i, img_interactiva, mensaje = 0, 0, 0, 'FUNCION 2 MAL ESCRITA'

    return {'solucion': x,
            'iteraciones': i,
            'tabla': tabla,
            'img_interactiva': img_interactiva,
            'mensaje': mensaje}


def puntofijo_test():

    #res = puntofijo_func('(e^x)-2', -2, 5, 3, 1e-20, 100)   # caso de fallo
    res = puntofijo_func('ahuevo', 'e**x-2', 1, 'Error absoluto', 1e-20, 200)

    for iteracion in res['tabla']:
        print(iteracion.i, iteracion.x, iteracion.fx, iteracion.err)

    print(res['mensaje'])
    print(f'Solución: {res["solucion"]}')
    print(f'Iteraciones: {res["iteraciones"]}')

    #show(res['img_interactiva'])

#puntofijo_test()
