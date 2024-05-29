from splineSegment import *


def spline_lineal(puntos):
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
    puntos = [(1, 2), (2, 3), (3, 5)]
    splines = spline_lineal(puntos)
    print(splines)


ejemplo()