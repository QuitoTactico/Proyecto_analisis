from math import *
from .base import func as base_func, func_deriv as base_func_deriv, graficar_template, grafico_interactivo
#from base import func as base_func, func_deriv as base_func_deriv, graficar_template, grafico_interactivo
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

def m1_func(funcion:str, m:int, a:float, b:float, x0:float, tol:float, niter:int):
    """
    Implementación método de Newton
    Entradas:
    funcion -- función
    funcionprima -- derivada función f
    x0 -- aproximación inicial
    tol -- tolerancia
    niter -- número máximo de iteraciones
    """

    def func(x): 
        return base_func(funcion, x)

    def funcprima(x): 
        return base_func_deriv(funcion, x)

    i = 1
    x_anterior, err, mensaje = None, 1, None
    tabla = []
    x0_inicial = x0

    tabla.append(Iteracion(0, 
                            f'{x0}', 
                            f'{func(x0)}', 
                            f'{1}'))

    while True:
        x = x0 - m*(func(x0)/funcprima(x0))
        fx = func(x)

        x_anterior = float(tabla[-1].x)
        err = abs(x - x_anterior)

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

    img_interactiva = grafico_interactivo(funcion, metodo='newton', sol=x, a=a, b=b, vlines= [('x0', x0_inicial)])

    return {'solucion'   : x, 
            'iteraciones': i, 
            'tabla'      : tabla,
            'img_interactiva': img_interactiva,
            'mensaje'    : mensaje
            }

def m1_test():
    #res = m1_func('(x^3)-10x-5', 2, -0.5, 4, 3, 1e-10, 100)
    res = m1_func('ln(x)*(x^2-4x+4)', 2, 1, 3, 1.5, 1e-16, 100)

    for iteracion in res['tabla']:
        print(iteracion)

    print(res['mensaje'])
    print(f'Solución: {res["solucion"]}')
    print(f'Iteraciones: {res["iteraciones"]}')

    show(res['img_interactiva'])

#m1_test()