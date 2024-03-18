from math import *
#from .base import func as base_func, graficar_template, grafico_interactivo
from base import func as base_func, graficar_template, grafico_interactivo
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

def puntofijo_func(funcion:str, funcion_g:str, a:float, b:float, x0:float, tol:float, niter:int):
    """
    Implementación método de punto fijo
    Entradas:
    funcion -- función
    x0 -- aproximación inicial
    tol -- tolerancia
    niter -- número máximo de iteraciones
    """

    def func(x): 
        return base_func(funcion_g, x)

    i = 1
    x_anterior, err, mensaje = None, 1, None
    tabla = []
    x0_inicial = x0

    while True:
        x = func(x0)
        fx = func(x)

        if i != 1:
            x_anterior = float(tabla[-1].x)
            err = abs(x - x_anterior)

        tabla.append(Iteracion(i, 
                            f'{x:.30f}', 
                            f'{fx:.30f}', 
                            f'{err:.30f}'))

        if abs(fx) <= 1e-64 or err <= tol:
            mensaje = 'PUNTO ENCONTRADO'
            break

        elif i >= niter:
            mensaje = 'ITERACIONES AGOTADAS'
            break

        else:
            x0 = x
            i += 1

    img_interactiva = grafico_interactivo(funcion, sol=x, a=a, b=b, vlines= [('x0', x0_inicial)], funcion_g=funcion_g)
    #img_interactiva = grafico_interactivo(funcion, sol=x, a=a, b=b, vlines= [('x0', x0_inicial)], funcion_g='NEWTON')

    return {'solucion'   : x, 
            'iteraciones': i, 
            'tabla'      : tabla,
            'img_interactiva': img_interactiva,
            'mensaje'    : mensaje
            }


def puntofijo_test():

    #res = puntofijo_func('(e^x)-2', -2, 5, 3, 1e-20, 100)   # caso de fallo
    res = puntofijo_func('(x^3)-10x-5', '(10x+5)^(1/3)', 0.5, 4, 1, 1e-20, 200)

    for iteracion in res['tabla']:
        print(iteracion.i, iteracion.x, iteracion.fx, iteracion.err)

    print(res['mensaje'])
    print(f'Solución: {res["solucion"]}')
    print(f'Iteraciones: {res["iteraciones"]}')

    show(res['img_interactiva'])

#puntofijo_test()