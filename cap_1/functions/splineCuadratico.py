#from cap_1.functions.spline_segment import *
from spline_segment import *


def spline_cuadratico(puntos):
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
    
    return splines


def ejemplo():
    # Ejemplo de uso:
    puntos = [(1, 2), (2, 3), (3, 5)]
    splines = spline_cuadratico(puntos)
    
    for i, spline in enumerate(splines):
        print(puntos[i], puntos[i+1])
        print(spline.function_str)


ejemplo()