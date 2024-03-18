from math import *
from .base import func as base_func, graficar_template, grafico_interactivo
from bokeh.plotting import show
#from base import func as base_func, graficar_template, grafico_interactivo

# CUANDO VAYAN A TESTEAR, COMENTEN EL SEGUNDO IMPORT Y DESCOMENTEN EL TERCERO

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
    
    i = 1
    x_anterior, err, mensaje_final = None, None, None
    a_inicial, b_inicial = a, b
    tabla = []

    while True:

        x = (b + a)/2
        fx = func(x)

        # En la primera iteración, estos valores no existen
        if i!=1:
            x_anterior = float(tabla[-1].x)
            err = abs(x - x_anterior)

        tabla.append(iteracion(i, 
                               f'{x:.30f}', 
                               f'{fx:.30f}', 
                               f'{err:.30f}' if i!=1 else None))
      
        # si f(x) = 0 o el error es menor que la tolerancia, terminamos
        
        # ya que el error no existe en la primera iteración, lo inicializamos para poder comparar
        if i == 1:  err = 1

        # 1e-64 es casi 0
        if abs(fx) <= 1e-64 or err <= tol:
            mensaje_final = 'PUNTO ENCONTRADO'
            break

        # si se pasó de iteraciones, también, pero no se encontró el punto.
        elif i >= niter:
            mensaje_final = 'ITERACIONES AGOTADAS'
            break
        # si no, seguimos
        else:
            if func(a)*fx > 0:
                a = x
            elif func(b)*fx > 0:
                b = x
            i += 1

    
    #img = graficar_template(funcion, sol=x, a=a, b=b, diplay_inicio=a-1, display_final=b+1)
    img = graficar_template(funcion, sol=x, a=a_inicial, b=b_inicial)
    img_interactiva = grafico_interactivo(funcion, sol=x, a=a_inicial, b=b_inicial)

    return {'solucion'   : x, 
            'iteraciones': i, 
            'tabla'      : tabla, 
            'img'        : img,
            'img_interactiva': img_interactiva,
            'mensaje'    : mensaje_final
            }

"""
def test_biseccion():


    # a = -2, b = 5, TOL = 1e-20, N0 = 100
    res = biseccion_func('(e^x)-2', -2, 5, 1e-20, 100)

    for iteracion in res['tabla']:
        print(iteracion.i, iteracion.x, iteracion.fx, iteracion.err)

    print(res['mensaje'])
    print(f'Solución: {res["solucion"]}')
    print(f'Iteraciones: {res['iteraciones']}')

    res['img'].show()
    show(res['img_interactiva'])


#test_biseccion()
"""