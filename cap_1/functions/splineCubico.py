from splineSegment import *


def spline_cubico(puntos):
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
    
    return splines


def ejemplo():
    # Ejemplo de uso:
    puntos = [(1, 2), (2, 3), (3, 5)]
    splines = spline_cubico(puntos)
    print(splines)


ejemplo()