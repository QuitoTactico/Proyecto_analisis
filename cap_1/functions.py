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

def graficar_template(expresion:str, x:float = 0, deriv:int=0, a:float = -5, b:float=5):
    expresion = expresion.replace("**", "^")
    x = sp.symbols('x')
    # i want the max y to be 100
    # i want the min y to be -100
    plot = sp.plot(expresion, (x, a, b), ylim=(-20, 20), line_color='r', show=False)
    # ahora graficamos la derivada
    if deriv == 1:
        plot.append(sp.plot(sp.diff(expresion, x), (x, a, b), line_color='g', show=False)[0])
    if deriv > 1:
        for i in range(deriv):
            plot.append(sp.plot(sp.diff(expresion, x, i), (x, a, b), line_color='g', show=False)[0])

    return plot
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

    x = float(input("Ingrese el valor de x: "))
    resultado = func(expresion, x)

    deriv = int(input("Ingrese el número de derivadas a calcular: "))
    
    print(expresion)
    print(resultado)

    plot = graficar_template(expresion, x, deriv)
    plot.show()

test()