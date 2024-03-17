from math import *
#from decimal import Decimal     # para precisión en los cálculos
import sympy as sp              # para las derivadas y graficación
import matplotlib.pyplot as plt # para graficar
import numpy as np

def estandarizar_expresion(expresion:str):
    '''Modificamos la expresión y la llevamos a una forma entendible por la función eval o la librería sympy, así se puede evaluar correctamente'''

    expresion = expresion.replace("^", "**").replace("sen", "sin").replace("tg", "tan").replace("ctg", "cot").replace('ln','log').lower()

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


def graficar_template_2(expresion:str, x:float = 0, deriv:int=0, a:float = -10, b:float=10):
    expresion = estandarizar_expresion(expresion)
    expresion = expresion.replace("**", "^").replace('e', 'E') # para que sympy entienda la expresión
    x = sp.symbols('x')

    inferior = min(a-1, -1)

    range = np.arange(a, b, 0.05)
    funcion_plot = [eval(expresion) for x in range]

    if 'fig' not in locals():
        fig, ax = plt.subplots()

    ax.plot(range, funcion_plot)
    #fig.savefig
    
    '''
    deriv_colors = ['g', 'b', 'y', 'c', 'm', 'k', 'r', 'g']
    
    # ahora graficamos las derivadas
    if deriv > 0:
        for i in range(deriv):
            ax.append(plt.plot(sp.diff(expresion, x, i+1), 
                                (x, a, b), 
                                xlim=(a-1, b+1), 
                                ylim=(inferior, b+1), 
                                line_color=deriv_colors[i], 
                                show=False
                                )[0]
                                )
    '''
    return ax
    #return sp.plot_implicit(sp.Eq(expresion, 0), (x, -2*sp.pi, 2*sp.pi), line_color='b', show=False)

def graficar_template(expresion:str, x:float = 0, deriv:int=0, a:float = -10, b:float=10):
    expresion = estandarizar_expresion(expresion)
    expresion = expresion.replace("**", "^").replace('e', 'E') # para que sympy entienda la expresión
    x = sp.symbols('x')

    inferior = min(a-1, -1)

    plot = sp.plot(expresion,
                   (x, a, b), 
                   xlim=(a-1, b+1), 
                   ylim=(inferior, b+1), 
                   line_color='r', 
                   show=False)

    deriv_colors = ['g', 'b', 'y', 'c', 'm', 'k', 'r', 'g']
    
    # ahora graficamos las derivadas
    if deriv > 0:
        for i in range(deriv):
            plot.append(sp.plot(sp.diff(expresion, x, i+1), 
                                (x, a, b), 
                                xlim=(a-1, b+1), 
                                ylim=(inferior, b+1), 
                                line_color=deriv_colors[i], 
                                show=False
                                )[0]
                                )

    return plot
    #return sp.plot_implicit(sp.Eq(expresion, 0), (x, -2*sp.pi, 2*sp.pi), line_color='b', show=False)


def func(expresion:str, x:float=0):
    expresion = estandarizar_expresion(expresion)
    resultado = eval(expresion)
    return resultado


def func_deriv(expresion, x:float=0, n_deriv:int=1):
    expresion = estandarizar_expresion(expresion)
    expresion = expresion.replace("**", "^").replace('e', 'E') # para que sympy entienda la expresión

    x = sp.symbols('x')
    derivada = sp.diff(expresion, x)
    return derivada

''' Deprecated
def func_2nd_deriv(expresion, x):
    expresion = estandarizar_expresion(expresion)

    expresion = expresion.replace("**", "^").replace('e', 'E')
    x = sp.symbols('x')
    derivada = sp.diff(expresion, x, 2)
    return derivada
'''

'''
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
    plot.save('static/img/test.png')


test()
'''