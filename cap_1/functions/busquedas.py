from math import *
from .base import func as base_func, graficar_template, grafico_interactivo
#from base import func as base_func, graficar_template, grafico_interactivo
from bokeh.plotting import show

class Iteracion:
    def __init__(self, i:int, x:str, fx:str):
        self.i = i
        self.x = x
        self.fx = fx

    def __str__(self):
        return f'{self.i} | {self.x} | {self.fx}'

    def __repr__(self):
        return f'{self.i} | {self.x} | {self.fx}'


def busquedas_func(funcion:str, x0:float, dx:float, niter:int):
    """
    Implementación método de búsqueda incremental
    Entradas:
    funcion -- función
    x0  -- inicio de búsqueda
    dx -- incremento
    niter -- número máximo de iteraciones
    """

    def func(x):
        return base_func(funcion, x)

    x0_inicial = x0
    f0 = func(x0)
    tabla = []
    i = 1

    while i < niter:
        x = x0 + dx
        fx = func(x)

        tabla.append(Iteracion(i,
                               f'{x:.25f}',
                               f'{fx:.25f}'))
        if f0*fx < 0:
            mensaje = 'PUNTO ENCONTRADO'
            break
    
        elif i >= niter:
            mensaje = 'ITERACIONES AGOTADAS'
            break

        x0 = x
        f0 = fx
        i +=1

    img_interactiva = grafico_interactivo(funcion, metodo='busquedas', sol=(x0+x)/2, a=x0_inicial, b=x, vlines=[('a', x0, 'blue'), ('b', x, 'blue')])

    return {'solucion'   : f"[{x0} , {x}], Punto: {(x0+x)/2}", 
            'iteraciones': i, 
            'tabla'      : tabla,
            'img_interactiva': img_interactiva,
            'mensaje'    : mensaje
            }


def test_busqueda_incremental():
    # a = -3, b = 10, dx = 0.2, niter = 100
    res = busquedas_func('x**3 - 10*x**2 + 5', -3, 0.2, 100)

    for iteracion in res['tabla']:
        print(iteracion)

    print(f'Solución: {res["solucion"]}')
    print(f'Iteraciones: {res["iteraciones"]}')

    show(res['img_interactiva'])

#test_busqueda_incremental()