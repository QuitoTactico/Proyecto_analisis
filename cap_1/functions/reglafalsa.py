from math import *
from .base import func as base_func, graficar_template, grafico_interactivo
#from base import func as base_func, graficar_template, grafico_interactivo

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

def reglafalsa_func(funcion:str, a:float, b:float, tol:float, niter:int):
    def func(x):
        return base_func(funcion, x)

    i = 1
    x_anterior, err, mensaje = None, 1, None
    a_inicial, b_inicial = a, b
    tabla = []

    if func(a)*func(b) > 0:
        mensaje, i, x = 'ERR: NO HAY CAMBIO DE SIGNO EN EL INTERVALO', 0, None
    else:
        while True:
            x = a-(func(a)*(b-a))/(func(b)-func(a))
            fx = func(x)

            if i!=1:
                x_anterior = float(tabla[-1].x)
                err = abs(x - x_anterior)

            tabla.append(Iteracion(i, 
                                f'{x:.30f}', 
                                f'{fx:.30f}', 
                                f'{err:.30f}' if i!=1 else None))

            if abs(fx) <= 1e-64 or err <= tol:
                mensaje = 'PUNTO ENCONTRADO'
                break

            elif i >= niter:
                mensaje = 'ITERACIONES AGOTADAS'
                break

            else:
                if func(a)*fx > 0:
                    a = x
                else:
                    b = x
                i += 1

    img_interactiva = grafico_interactivo(funcion, sol=x, a=a_inicial, b=b_inicial)

    return {'solucion'   : x, 
            'iteraciones': i, 
            'tabla'      : tabla,
            'img_interactiva': img_interactiva,
            'mensaje'    : mensaje
            }

def test_regla_falsa():
    from bokeh.plotting import show

    res = reglafalsa_func('exp(x) + 3*cos(x)', -4, 2, 1e-20, 100)

    for iteracion in res['tabla']:
        print(iteracion)

    print(res['mensaje'])
    print(f'Solución: {res["solucion"]}')
    print(f'Iteraciones: {res["iteraciones"]}')

    show(res['img_interactiva'])

#test_regla_falsa()