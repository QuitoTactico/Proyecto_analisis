from cap_1.functions.spline_segment import *
#from spline_segment import *
from .base import func as base_func, func_deriv as base_func_deriv, graficar_template, grafico_interactivo
#from base import func as base_func, func_deriv as base_func_deriv, graficar_template, grafico_interactivo
from bokeh.plotting import show

def spline_cuadratico(x, y):

    try:
            x = [float(num) for num in x.strip("[]").split()]
            y = [float(num) for num in y.strip("[]").split()]
    except ValueError as e:
            return {'mensaje': f"Input parsing error: {e}"}, None

    if not is_ascending(x):
         return {'mensaje': f"Input x-values must be sorted in increasing order"}, None
    
    if len(x) != len(y):
         return {'mensaje': f"Input vectors x and y must have the same length"}, None
    
    puntos = list(zip(x,y))

    n = len(puntos) - 1
    splines = []
    
    for i in range(n):
        x0, y0 = puntos[i]
        x1, y1 = puntos[i + 1]
        
        a = (y1 - y0) / ((x1 - x0) ** 2)
        b = -2 * a * x0
        c = y0 + a * x0 ** 2
        function_str = f"{a} * x^2 + {b} * x + {c}"
        
        spline = SplineSegment(i, a, b, c, function_str=function_str)
        splines.append(spline)
    
    img_interactiva = grafico_interactivo(metodo='spline', a=x[0], b=x[-1], puntos=puntos, splines=splines)
    return splines, img_interactiva


def ejemplo():
    # Ejemplo de uso:
    x = '[1 2 3 5]'
    y = '[2 3 5 1]'
    splines, img_interactiva = spline_cuadratico(x, y)
    show(img_interactiva)
    '''
    for i, spline in enumerate(splines):
        print(puntos[i], puntos[i+1])
        print(spline.function_str)
    '''


#ejemplo()