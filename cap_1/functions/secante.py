from math import *
from .base import func as base_func, grafico_interactivo
#from base import func as base_func, grafico_interactivo
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

def secante_func(funcion:str, a:float, b:float, x0:float, x1:float, tol:float, niter:int):
    """
    Implementación método de la secante
    Entradas:
    funcion -- función
    x0 -- aproximación inicial
    x1 -- segunda aproximación inicial
    tol -- tolerancia
    niter -- número máximo de iteraciones
    """

    def func(x): 
        return base_func(funcion, x)

    i = 2
    err, mensaje = 1, None
    tabla = []

    tabla.append(Iteracion(0, 
                            f'{x0:.30f}', 
                            f'{func(x0):.30f}', 
                            f'{1:.30f}'))
    tabla.append(Iteracion(1, 
                            f'{x1:.30f}', 
                            f'{func(x1):.30f}', 
                            f'{abs(x1 - x0):.30f}'))

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
        
        err = abs(x - x1)

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
            x0 = x1
            x1 = x
            i += 1

    img_interactiva = grafico_interactivo(funcion, metodo='secante', sol=x, a=a, b=b, vlines= [('x0', x0), ('x1', x1)])


    return {'solucion'   : x, 
            'iteraciones': i, 
            'tabla'      : tabla,
            'img_interactiva': img_interactiva,
            'mensaje'    : mensaje
            }

def secante_test():
    res = secante_func(funcion='(x^3)-10x-5', a=-0.5, b=4, x0=3, x1=2, tol=1e-10, niter=100)

    for iteracion in res['tabla']:
        print(iteracion)

    print(res['mensaje'])
    print(f'Solución: {res["solucion"]}')
    print(f'Iteraciones: {res["iteraciones"]}')

    show(res['img_interactiva'])

#secante_test()
