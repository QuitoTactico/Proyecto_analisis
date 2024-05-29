#from cap_1.functions.spline_segment import *
from spline_segment import *
#from .base import func as base_func, func_deriv as base_func_deriv, graficar_template, grafico_interactivo
from base import func as base_func, func_deriv as base_func_deriv, graficar_template, grafico_interactivo
from bokeh.plotting import show

def spline_cubico(x, y):

    try:
            x = [float(num) for num in x.strip("[]").split()]
            y = [float(num) for num in y.strip("[]").split()]
    except ValueError as e:
            return {'mensaje': f"Input parsing error: {e}"}

    if not is_ascending(x):
         return {'mensaje': f"Input x-values must be sorted in increasing order"}
    
    if len(x) != len(y):
         return {'mensaje': f"Input vectors x and y must have the same length"}
    
    puntos = list(zip(x,y))

    n = len(puntos) - 1
    splines = []
    
    for i in range(n):
        x0, y0 = puntos[i]
        x1, y1 = puntos[i + 1]
        
        a = (y1 - y0) / ((x1 - x0) ** 3)
        b = -3 * a * x0
        c = 3 * a * x0 ** 2
        d = y0 - a * x0 ** 3
        function_str = f"{a} * x^3 + {b} * x^2 + {c} * x + {d}"
        
        spline = SplineSegment(i, a, b, c, d, function_str=function_str)
        splines.append(spline)
    
    img_interactiva = grafico_interactivo(metodo='spline', a=x[0], b=x[-1], puntos=puntos, splines=splines)
    return splines, img_interactiva


def ejemplo():
    # Ejemplo de uso:
    x = '[1 2 3 5]'
    y = '[2 3 5 1]'
    splines, img_interactiva = spline_cubico(x, y)
    show(img_interactiva)

    '''
    for i, spline in enumerate(splines):
        print(puntos[i], puntos[i+1])
        print(spline.function_str)
    '''

ejemplo()