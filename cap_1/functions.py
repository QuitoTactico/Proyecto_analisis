from math import *
from decimal import Decimal     # para precisión en los cálculos
import sympy as sp              # para las derivadas y graficación


def estandarizar_expresion(expresion:str):
    '''Modificamos la expresión y la llevamos a una forma entendible por la función eval o la librería sympy, así se puede evaluar correctamente'''

    expresion = expresion.replace("^", "**").replace("sen", "sin").replace("tg", "tan").replace("ctg", "cot").lower()

    # aunque en la vida real escribamos 2x, para ser entendido se debe escribir 2*x. 
    # no es el único caso, puede suceder lo mismo con euler, pi, etc. 
    # incluso entre ellos mismos, como en el caso de xe, que se debe escribir x*e
    i = 0
    while i < len(expresion):
        if i>0:
            if expresion[i] in ["x","e","pi"] and (expresion[i-1].isdigit() or expresion[i-1] in [")","x","e","pi"]):
                expresion = expresion[:i] + "*" + expresion[i:]
            if expresion[i].isdigit() and expresion[i-1] in [")","x","e","pi"]:
                expresion = expresion[:i] + "*" + expresion[i:]
        i += 1
    return expresion


def graficar(expresion:str, x, a:float = -20, b:float=20):
    expresion = expresion.replace("**", "^")
    x = sp.symbols('x')
    return sp.plot(expresion, (x, -2*sp.pi, 2*sp.pi), line_color='r', show=False)
    #return sp.plot_implicit(sp.Eq(expresion, 0), (x, -2*sp.pi, 2*sp.pi), line_color='b', show=False)

def func(expresion:str, x:Decimal):
    resultado = eval(expresion)
    return resultado

def func_deriv(expresion, x:Decimal):
    x = sp.symbols('x')
    derivada = sp.diff(expresion, x)
    return derivada

def func_2nd_deriv(expresion, x):
    x = sp.symbols('x')
    derivada = sp.diff(expresion, x, 2)
    return derivada

def test():
    expresion_original = input("Ingrese la expresión a evaluar: ")
    expresion = estandarizar_expresion(expresion_original)
    print(expresion)

    x = float(input("Ingrese el valor de x: "))
    resultado = func(expresion, x)
    
    print(resultado)

    plot = graficar(expresion, x)
    plot.show()

test()