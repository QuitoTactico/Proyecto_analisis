import math
import sympy as sp
import numpy as np
import pandas as pd

def bisection(f, a, b, tol=1e-2, max_iter=100):
    #c va a ser la aproximación a 0 de f
    c = a
    tabla = []  # Inicializa la tabla como una lista vacía
    for _ in range(max_iter):
        c = (a + b) / 2
        errorabsoluto = abs(a - b)
        errorrelativo = errorabsoluto / c
        if f(c) == 0 or abs(a - b) < tol:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        # Agrega una fila a la tabla
        tabla.append({"a": a, "b": b, "c": c, "f(c)": f(c), "ErrorAbsoluto": errorabsoluto, "ErrorRelativo": errorrelativo})
        print(tabla)
    return tabla

def fixed_point(g, x0, tol=1e-2, max_iter=100):
    x = x0
    iteraciones = 0
    tablapuntofijo = []  # Inicializa la tabla como una lista vacía
    for _ in range(max_iter):
        iteraciones += 1
        x1 = g(x)
        errorABS = abs(x1 - x)
        errorRelativo = errorABS / x1

        # Agrega una fila a la tabla
        tablapuntofijo.append({"Iteracion": iteraciones, "x": x, "x1": x1, "Error": errorABS, "ErrorRelativo": errorRelativo})
        if errorABS < tol and errorRelativo< tol:
            break
        x = x1
    return tablapuntofijo

"""
def false_position(f, a, b, tol=1e-2, max_iter=100):
    c = a
    tabla = []  # Inicializa la tabla como una lista vacía
    fa = f(a)
    fb = f(b)
    for _ in range(max_iter):
        c = a*fb - b*fa / (fb - fa)
        if f(c) == 0 or abs(c-b) < tol:
            break
        elif c*b < 0:
            a = b
            fa = fb
        b = c
        fb = f(c)
        tabla.append({"a": a, "b": b, "c": c, "f(c)": f(c)})
    return tabla
"""
def false_position(f, p0, p1, tol=1e-2, max_iter=100):
    i = 0
    tabla = []  # Inicializa la tabla como una lista vacía
    while i < max_iter:
        q0 = f(p0)
        q1 = f(p1)
        p = p1 - q1*(p1 - p0)/(q1 - q0)
        if abs(p - p1) < tol:
            break
        i += 1
        ErrorAbsoluto = abs(p1 - p)
        ErrorRelativo = ErrorAbsoluto / p1
        if f(p)*f(p1) < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = f(p)
        tabla.append({"p0": p0, "p1": p1, "p": p, "f(p)": f(p), "ErrorAbsoluto": ErrorAbsoluto, "ErrorRelativo": ErrorRelativo})
        
    return tabla  # Siempre devuelve la tabla



def newton(f, x0, tol=1e-5, max_iter=100):
    x = sp.symbols('x')  # Define x como un símbolo
    f_sym = f(x)  # Convierte f en una expresión simbólica
    df_sym = sp.diff(f_sym, x)  # Deriva f_sym con respecto a x

    # Convierte f_sym y df_sym en funciones de Python que puedes evaluar
    f = sp.lambdify(x, f_sym, 'numpy')
    df = sp.lambdify(x, df_sym, 'numpy')

    x = x0
    tabla = []  # Inicializa la tabla como una lista vacía
    for _ in range(max_iter):
        x1 = x - f(x) / df(f)
        if abs(x1 - x) < tol:
            break
        ErrorAbsoluto = abs(x1 - x)
        ErrorRelativo = ErrorAbsoluto / x1

        tabla.append({"x": x, "f(x)": f(x), "f'(x)": df(x), "x1": x1, "ErrorAbsoluto": ErrorAbsoluto, "ErrorRelativo": ErrorRelativo})
        
        x = x1
    return tabla  # Siempre devuelve la tabla
"""
def secant(f, x0, x1, tol=1e-5, max_iter=100):
    for _ in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0 = x1
        x1 = x2
    return x2

def steffensen(f, x0, tol=1e-5, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x1 = f(x)
        x2 = f(x1)
        x3 = x - (x1 - x)**2 / (x2 - 2 * x1 + x)
        if abs(x3 - x) < tol:
            return x3
        x = x3
    return x
"""
def main():
    f = lambda x: 2*np.exp(x**2)- 5*x
    #f = lambda x: x**2 -4
    g = lambda x: 0.4*np.exp(x**2)
    #g = lambda x: math.sqrt(4)
    x0 = 0.01
    a = 0
    b = 1
    print("elija metodo:")
    print("1. punto fijo")
    print("2. biseccion")
    print("3. falsa posicion")
    print("4. newton")
    opcion = int(input("ingrese el metodo: "))
    if(opcion == 1):
        print("metodo punto fijo")
        tablapuntofijo = fixed_point(g, x0)
        dfpunto = pd.DataFrame(tablapuntofijo)
        print(dfpunto)

    elif(opcion == 2):
        print("metodo biseccion")
        tablabiseccion = bisection(f, a, b)
        dfbiseccion = pd.DataFrame(tablabiseccion)
        print(dfbiseccion)
    elif(opcion == 3):
        print("metodo falsa posicion")
        c = false_position(f, a, b)
        dffalsaposicion = pd.DataFrame(c)
        print(dffalsaposicion)
    elif(opcion == 4):
        print("metodo newton")
        x = newton(f, x0)
        dfnewton = pd.DataFrame(x)
        print(dfnewton)


main()