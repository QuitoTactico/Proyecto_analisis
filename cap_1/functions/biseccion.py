from math import *
from .base import func as base_func, graficar_template, grafico_interactivo
#from base import func as base_func, graficar_template, grafico_interactivo
from bokeh.plotting import show

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


def biseccion_func(funcion:str, a:float, b:float,error_type:str, tol:float, niter:int):
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
    x_anterior, err, mensaje = None, 1, None
    a_inicial, b_inicial = a, b
    tabla = []

    if func(a)*func(b) > 0:
        mensaje, i, x = 'ERR: NO HAY CAMBIO DE SIGNO EN EL INTERVALO', 0, None
    else:
        while True:

            x = (b + a)/2
            fx = func(x)

            # En la primera iteración, estos valores no existen
            if i!=1:
                x_anterior = float(tabla[-1].x)
                if error_type == 'Error absoluto':
                    err = abs(x - x_anterior)
                elif error_type == 'Error relativo':
                    err = abs((x - x_anterior)/x)

            tabla.append(iteracion(i, 
                                f'{x}', 
                                f'{fx}', 
                                f'{err}'))
        
            # si f(x) = 0 o el error es menor que la tolerancia, terminamos
            
            # ya que el error no existe en la primera iteración, lo inicializamos para poder comparar
            #if i == 1:  err = 1    # pusimos err = 1 antes del while

            # 1e-64 es casi 0. Realmente float solo guarda 16 digitos, pero lo dejamos así en caso de que usemos una alternativa, como decimal.Decimal 
            if abs(fx) <= 1e-64 or err <= tol:
                mensaje = 'PUNTO ENCONTRADO'
                break

            # si se pasó de iteraciones, también, pero no se encontró el punto.
            elif i >= niter:
                mensaje = 'ITERACIONES AGOTADAS'
                break
            # si no, seguimos
            else:
                if func(a)*fx > 0:
                    a = x
                elif func(b)*fx > 0:
                    b = x
                i += 1

    
    #img = graficar_template(funcion, sol=x, a=a, b=b, diplay_inicio=a-1, display_final=b+1)
    #img = graficar_template(funcion, sol=x, a=a_inicial, b=b_inicial)
    img_interactiva = grafico_interactivo(funcion, sol=x, a=a_inicial, b=b_inicial)

    return {'solucion'   : x, 
            'iteraciones': i, 
            'tabla'      : tabla,
            'img_interactiva': img_interactiva,
            'mensaje'    : mensaje
            }


def test_biseccion():
    # a = -2, b = 5, TOL = 1e-20, N0 = 100
    #res = biseccion_func('(e^x)-2', -2, 5, 1e-20, 100)
    res = biseccion_func('x^5 - x^4 + 2*x^3 - x^2 + x - 1', -2, 2, 'Error relativo', 1e-20, 100)

    for iteracion in res['tabla']:
        print(iteracion.i, iteracion.x, iteracion.fx, iteracion.err)

    print(res['mensaje'])
    print(f'Solución: {res["solucion"]}')
    print(f'Iteraciones: {res["iteraciones"]}')

    res['img'].show()
    show(res['img_interactiva'])


#test_biseccion()
