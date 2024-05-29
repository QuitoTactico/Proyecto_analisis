#from cap_1.functions.spline_segment import *
from spline_segment import *


def spline_lineal(x, y):

    try:
            x = [float(num) for num in x.strip("[]").split()]
            y = [float(num) for num in y.strip("[]").split()]
    except ValueError as e:
            return {'mensaje': f"Input parsing error: {e}"}

    if not is_ascending(x):
         return {'mensaje': f"Input x-values must be sorted in increasing order"}
    
    if len(x) != len(y):
         return {'mensaje': f"Input vectors x and y must have the same length"}
    
    puntos = zip(x,y)

    n = len(puntos) - 1
    splines = []
    
    for i in range(n):
        x0, y0 = puntos[i]
        x1, y1 = puntos[i + 1]
        
        a = (y1 - y0) / (x1 - x0)
        b = y0 - a * x0
        function_str = f"{a} * x + {b}"
        
        spline = SplineSegment(i=i, coef1=a, coef2=b, function_str=function_str)
        splines.append(spline)
    
    return splines


def ejemplo():
    # Ejemplo de uso:
    puntos = [(1, 2), (2, 3), (3, 5), (5, 1)]
    splines = spline_lineal(puntos)

    for i, spline in enumerate(splines):
        print(puntos[i], puntos[i+1])
        print(spline.function_str)


#ejemplo()