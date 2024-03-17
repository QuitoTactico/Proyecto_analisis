from math import *
#from decimal import Decimal     # para precisión en los cálculos
import sympy as sp              # para las derivadas y graficación
#import matplotlib.pyplot as plt
#import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import Span, Legend, LegendItem

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


def graficar_template(expresion:str, sol:float=0, a:float=-10, b:float=10, deriv:int=0, display_inicio=None, display_final=None):

    # si no se especifica el display, se toma el centro del intervalo para centrar la gráfica
    centro = (a+b)/2
    if display_inicio == display_final:
        display_inicio = centro-a
        display_final = centro+b
    elif display_inicio == None:
        display_inicio = centro-a
    elif display_final == None:
        display_final = centro+b

    expresion = estandarizar_expresion(expresion)
    expresion = expresion.replace("**", "^").replace('e', 'E') # para que sympy entienda la expresión
    x = sp.symbols('x')

    # intenté escalar los ejes en 1:1, pero es más importante poder ver el 0
    inferior = min(display_inicio, -1)

    plot = sp.plot(expresion,
                   (x, a, b),
                   #xlim=(display_inicio, display_final),
                   #ylim=(inferior, display_final),
                   line_color='r', 
                   show=False)
    
    '''
    plot = sp.plot(expresion,
                   (x, a, b), 
                   xlim=(diplay_inicio, display_final), 
                   ylim=(inferior, display_final), 
                   line_color='r', 
                   show=False)
    '''

    deriv_colors = ['g', 'b', 'y', 'c', 'm', 'k', 'r', 'g']
    
    # ahora graficamos las derivadas
    if deriv > 0:
        for i in range(deriv):
            plot.append(sp.plot(sp.diff(expresion, x, i+1), 
                                (x, a, b), 
                                #xlim=(display_inicio, display_final), 
                                #ylim=(inferior, display_final),
                                line_color=deriv_colors[i], 
                                show=False)[0])

    # línea marcando la solución. Tocó agregar 3 líneas para que se grueso, a mano, terrible
    plot.append(sp.plot_implicit(sp.Eq(x, sol), line_color='r', show=False)[0])
    plot.append(sp.plot_implicit(sp.Eq(x, sol+0.04), line_color='r', show=False)[0])
    plot.append(sp.plot_implicit(sp.Eq(x, sol-0.05), line_color='r', show=False)[0])

    # líneas marcando los bordes
    plot.append(sp.plot_implicit(sp.Eq(x, a), line_color='g', show=False)[0])
    plot.append(sp.plot_implicit(sp.Eq(x, b), line_color='g', show=False)[0])

    return plot
    #return sp.plot_implicit(sp.Eq(expresion, 0), (x, -2*sp.pi, 2*sp.pi), line_color='b', show=False)


# hecho con matplotlib, pero no era necesario
''' deprecated
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
    
    return ax
    #return sp.plot_implicit(sp.Eq(expresion, 0), (x, -2*sp.pi, 2*sp.pi), line_color='b', show=False)
'''
    
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

def grafico_interactivo_basic(plot=None, sol=None, a=None, b=None):
    plot_interactivo = figure(active_scroll='wheel_zoom')
    
    colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'black']
    # Agregar líneas al gráfico
    for i, color in enumerate(colors):
        # Aquí puedes reemplazar [i, i+1, i+2] y [i, i**2, i**3] con tus propios datos
        line = plot_interactivo.line([i, i+1, i+2], [i, i**2, i**3], line_color=color, line_width=2)

        # Agregar la línea a la leyenda
        plot_interactivo.add_layout(Legend(items=[LegendItem(label=color, renderers=[line])]))

    # Agregar líneas verticales en a y b
    vline = Span(location=3, dimension='height', line_color='green', line_width=2)
    plot_interactivo.add_layout(vline)
    # configures the lasso tool to be active

    # Mostrar el gráfico
    #show(plot_interactivo)
    return plot_interactivo


def grafico_interactivo(plot=None, sol:float=None, a:float=None, b:float=None, deriv:int=0):
    plot_interactivo = figure(active_scroll='wheel_zoom')

    colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'black']
    lista_leyenda = []
    for i in range(deriv+1):
        funcion = plot_interactivo.line(plot[i].get_points()[0], plot[i].get_points()[1], line_color=colors[i], line_width=2)

        lista_leyenda.append(LegendItem(label='f'+"'"*i+'(x)', renderers=[funcion]))
        
    # agregar línea en la solución
    vline = Span(location=sol, dimension='height', line_color='black', line_width=1, line_dash='dashed')
    plot_interactivo.add_layout(vline)
    # para ponerla en la leyenda, tocó poner una línea invisible
    invisible = plot_interactivo.line([0], [0], line_color="black", line_dash='dashed')   
    lista_leyenda.append(LegendItem(label='Solución', renderers=[invisible]))


    # agregar líneas en a y b
    if a != None and b != None:
        vline = Span(location=a, dimension='height', line_color='green', line_width=2, line_dash='dashed')
        plot_interactivo.add_layout(vline)
        vline = Span(location=b, dimension='height', line_color='green', line_width=2, line_dash='dashed')
        plot_interactivo.add_layout(vline)

        # otra línea invisible línea invisible
        invisible = plot_interactivo.line([0], [0], line_color="green", line_width=1, line_dash='dashed')   
        lista_leyenda.append(LegendItem(label='Bordes', renderers=[invisible]))

    plot_interactivo.add_layout(Legend(items=lista_leyenda))
    plot_interactivo.aspect_scale = 1       # para que los ejes tengan la misma escala, 1:1
    plot_interactivo.xaxis.visible = True   # para que se vean los ejes
    plot_interactivo.yaxis.visible = True
    
    return plot_interactivo


def test_base():
    expresion_original = input("Ingrese la expresión a evaluar: ")
    expresion = estandarizar_expresion(expresion_original)

    x = float(input("Ingrese el valor de x: "))
    sol = func(expresion, x)

    deriv = int(input("Ingrese el número de derivadas a calcular: "))
    
    print(expresion)
    print(sol)

    plot = graficar_template(expresion, x, deriv=deriv)
    plot.show()
    plot.save('static/img/test.png')


def test_interactivo():
    expresion_original = input("Ingrese la expresión a evaluar: ")
    expresion = estandarizar_expresion(expresion_original)

    x = float(input("Ingrese el valor de x: "))
    sol = func(expresion, x)
    
    a,b = map(float, input("Ingrese el intervalo a evaluar (a   b): ").split(" "))

    deriv = int(input("Ingrese el número de derivadas a calcular: "))
    
    print(expresion)
    print(sol)

    plot = graficar_template(expresion, sol, deriv=deriv)
    plot_interactivo = grafico_interactivo(plot, sol, a, b, deriv=deriv)
    show(plot_interactivo)


#test_base()
#test_interactivo()
