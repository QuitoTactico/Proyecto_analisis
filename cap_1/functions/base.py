from math import *
import sympy as sp                                  # para las derivadas y graficación PNG
from bokeh.plotting import figure, show             # para la graficación interactiva
from bokeh.models import Span, Legend, LegendItem, CrosshairTool, HoverTool, ZoomInTool, ZoomOutTool, ExamineTool, Range1d

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

    # línea marcando la solución. Tocó agregar 3 líneas para que se vea grueso, a mano, terrible
    plot.append(sp.plot_implicit(sp.Eq(x, sol), line_color='r', show=False)[0])
    #plot.append(sp.plot_implicit(sp.Eq(x, sol+0.04), line_color='r', show=False)[0])
    #plot.append(sp.plot_implicit(sp.Eq(x, sol-0.05), line_color='r', show=False)[0])

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
    #derivada = sp.diff(expresion, x, n_deriv).evalf(subs={x: x})
    derivada = sp.diff(expresion, x, n_deriv)
    return float(derivada)


def grafico_interactivo(funcion='2x-1', sol:float=None, a:float=None, b:float=None, deriv:int=0):
    '''Grafica la función y sus derivadas, con líneas punteadas en a y b, y una línea punteada en la solución si es que se especifica'''

    distancia = abs(b-a)

    plot_interactivo = figure(active_scroll='wheel_zoom', 
                              aspect_scale = 1, 
                              #x_range=(a-distancia_media/2, b+distancia_media/2), 
                              #y_range=(distancia_media*(-1.5), distancia_media*1.5), 
                              match_aspect=True, 
                              sizing_mode='stretch_both', 
                              x_axis_label='x', 
                              y_axis_label='f(x)')
    
    # identificamos con esta función charra que hice el rango de la gráfica. Pero si no se encontró solución, es
    # mejor dejarlo con el autoático de la gráfica, porque de seguro algo raro pasó con esa función, y así podremos verlo
    if sol is not None:
        plot_interactivo.x_range = Range1d(a-(distancia*0.2), b+(distancia*0.2))
        plot_interactivo.y_range = Range1d(float(-distancia)/1.7, distancia/1.7)


    width = Span(dimension="width", line_dash="dotted", line_alpha=0.4, line_width=1)
    height = Span(dimension="height", line_dash="dotted", line_alpha=0.4, line_width=1)
    plot_interactivo.add_tools(CrosshairTool(overlay=[width, height]))
    plot_interactivo.add_tools(HoverTool(tooltips= [("name", "$name"),
                                                    ("x",    "$x"),
                                                    ("y", "@y")],
                                         mode='vline'))
    plot_interactivo.add_tools(ZoomInTool(factor=0.25))
    plot_interactivo.add_tools(ZoomOutTool(factor=0.25))
    plot_interactivo.add_tools(ExamineTool())  # to debug

    colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'black']
    lista_leyenda = []

    # graficaremos la función y sus derivadas
    for i in range(deriv+1):
        # 200 puntos entre a y b
        eje_x = [a + (b-a)/200 * i for i in range(201)]
        # para cada punto: si es la primera iteración, les evaluamos la función normal, si no, la derivada i-ésima
        eje_y = [func(funcion, x) for x in eje_x] if i == 0 else [func_deriv(funcion, x, i) for x in eje_x]

        funcion_linea = plot_interactivo.line(eje_x, eje_y, line_color=colors[i], line_width=2, name='f'+"'"*i+'(x)')
        lista_leyenda.append(LegendItem(label='f'+"'"*i+'(x)', renderers=[funcion_linea]))
        

    # agregar líneas en a y b
    if a is not None and b is not None:
        vline = Span(location=a, dimension='height', line_color='green', line_width=1, line_dash='dashed')
        plot_interactivo.add_layout(vline)
        vline = Span(location=b, dimension='height', line_color='green', line_width=1, line_dash='dashed')
        plot_interactivo.add_layout(vline)

        # otra línea invisible línea invisible
        invisible = plot_interactivo.line([0], [0], line_color="green", line_width=1, line_dash='dashed')   
        lista_leyenda.append(LegendItem(label='Bordes', renderers=[invisible]))

    if sol is not None:
        # agregar línea en la solución
        vline = Span(location=sol, dimension='height', line_color='black', line_width=1, line_dash='dashed')
        plot_interactivo.add_layout(vline)
        # para ponerla en la leyenda, tocó poner una línea invisible
        invisible = plot_interactivo.line([0], [0], line_color="black", line_dash='dashed')   
        lista_leyenda.append(LegendItem(label='Solución', renderers=[invisible]))
        # también un punto
        plot_interactivo.scatter([sol], [0], fill_color='red', line_color="black", size=8, name="Solución")

    plot_interactivo.add_layout(Legend(items=lista_leyenda))

    # btw esto del 1:1 simplemente no quiere funcionar. Horas gastadas aquí: (4)
    #plot_interactivo.set(x_range=[a, b], y_range=[a, b], match_aspect=True)
    plot_interactivo.aspect_scale = 1       # para que los ejes tengan la misma escala, 1:1
    plot_interactivo.xaxis.visible = True   # para que se vean los ejes
    plot_interactivo.yaxis.visible = True
    plot_interactivo.xaxis.fixed_location = 0   # para que el eje x pase por y=0 y no esté en el borde del grafico
    plot_interactivo.yaxis.fixed_location = 0   # para que el eje y pase por x=0 y no esté en el borde del grafico
    plot_interactivo.match_aspect = True        # otro intento de hacer que tengan la misma escala, 1:1
    
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
    
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))

    deriv = int(input("Ingrese el número de derivadas a calcular: "))
    
    print(expresion)
    print(sol)

    plot = graficar_template(expresion, sol=sol, deriv=deriv)
    plot_interactivo = grafico_interactivo(expresion, sol=sol, a=a, b=b, deriv=deriv)
    show(plot_interactivo)


#test_base()
#test_interactivo()
