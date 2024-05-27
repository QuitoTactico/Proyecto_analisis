from django.shortcuts import render
from django.http import HttpResponse
from .functions.busquedas import busquedas_func
from .functions.biseccion import biseccion_func
from .functions.reglafalsa import reglafalsa_func
from .functions.puntofijo import puntofijo_func
from .functions.newton import newton_func
from .functions.secante import secante_func
from .functions.m1 import m1_func
# Create your views here.

import matplotlib.pyplot as plt
import matplotlib
import io 
import urllib, base64
from bokeh.embed import components

def home(request):
    return render(request, 'index.html')

def maquina(request):
    return render(request, 'maquina.html')

def busquedas(request):
    if request.method == 'POST':
        funcion = request.POST['funcion']
        x0 = float(request.POST['x0'])
        dx = float(request.POST['dx'])
        niter = int(request.POST['niter'])

        response = busquedas_func(funcion, x0, dx, niter)

        img_interactiva = response['img_interactiva']
        script, div = components(img_interactiva)

        return render(request, 'busquedas.html', {'solucion'  : response['solucion'], 
                                            'iteraciones' : response['iteraciones'],
                                            'tabla': response['tabla'],
                                            'img_interactiva': img_interactiva,
                                            'script': script, 'div': div,
                                            'mensaje': response['mensaje']})
    else:
        return render(request, 'busquedas.html')


def biseccion(request):

    if request.method == 'POST':
        matplotlib.use('Agg')

        funcion = request.POST['funcion']
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])

        response = biseccion_func(funcion, a, b, tol, niter)

        """
        img = response['img']
        buffer = io.BytesIO()
        img.save(buffer)
        buffer.seek(0) 
        image_png = buffer.getvalue() 
        buffer.close() 
        img = base64.b64encode(image_png) 
        img = img.decode('utf-8') 
        """

        img_interactiva = response['img_interactiva']
        script, div = components(img_interactiva)

        return render(request, 'biseccion.html', {'solucion'  : response['solucion'], 
                                             'iteraciones' : response['iteraciones'],
                                             'tabla': response['tabla'],
                                             'img_interactiva': img_interactiva,
                                             'script': script, 'div': div,
                                             'mensaje': response['mensaje']})
    else:
        return render(request, 'biseccion.html')
    
def reglafalsa(request):
    
        if request.method == 'POST':
            funcion = request.POST['funcion']
            a = float(request.POST['a'])
            b = float(request.POST['b'])
            tol = float(request.POST['tol'])
            niter = int(request.POST['niter'])
    
            response = reglafalsa_func(funcion, a, b, tol, niter)
    
            img_interactiva = response['img_interactiva']
            script, div = components(img_interactiva)
    
            return render(request, 'reglafalsa.html', {'solucion'  : response['solucion'], 
                                                'iteraciones' : response['iteraciones'],
                                                'tabla': response['tabla'],
                                                'img_interactiva': img_interactiva,
                                                'script': script, 'div': div,
                                                'mensaje': response['mensaje']})
        else:
            return render(request, 'reglafalsa.html')
    

def puntofijo(request):

    if request.method == 'POST':
        funcion = request.POST['funcion']
        funcion_g = request.POST['funcion_g']
        x0 = float(request.POST['x0'])
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])

        response = puntofijo_func(funcion, funcion_g, a, b, x0, tol, niter)

        img_interactiva = response['img_interactiva']
        script, div = components(img_interactiva)

        return render(request, 'puntofijo.html', {'solucion'  : response['solucion'], 
                                             'iteraciones' : response['iteraciones'],
                                             'tabla': response['tabla'],
                                             'img_interactiva': img_interactiva,
                                             'script': script, 'div': div,
                                             'mensaje': response['mensaje']})
    else:
        return render(request, 'puntofijo.html')

def newton(request):
    if request.method == 'POST':
        funcion = request.POST['funcion']
        x0 = float(request.POST['x0'])
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])

        response = newton_func(funcion, a, b, x0, tol, niter)

        img_interactiva = response['img_interactiva']
        script, div = components(img_interactiva)

        return render(request, 'newton.html', {'solucion'  : response['solucion'], 
                                            'iteraciones' : response['iteraciones'],
                                            'tabla': response['tabla'],
                                            'img_interactiva': img_interactiva,
                                            'script': script, 'div': div,
                                            'mensaje': response['mensaje']})
    else:
        return render(request, 'newton.html')
        
def secante(request):
     
    if request.method == 'POST':
        funcion = request.POST['funcion']
        x0 = float(request.POST['x0'])
        x1 = float(request.POST['x1'])
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])

        response = secante_func(funcion, a, b, x0, x1, tol, niter)

        img_interactiva = response['img_interactiva']
        try:
            script, div = components(img_interactiva)
        except:
            script, div = None, None

        return render(request, 'secante.html', {'solucion'  : response['solucion'], 
                                            'iteraciones' : response['iteraciones'],
                                            'tabla': response['tabla'],
                                            'img_interactiva': img_interactiva,
                                            'script': script, 'div': div,
                                            'mensaje': response['mensaje']})
    else:
        return render(request, 'secante.html')

def m1(request):
    if request.method == 'POST':
        funcion = request.POST['funcion']
        x0 = float(request.POST['x0'])
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        m = float(request.POST['m'])
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])

        response = m1_func(funcion, m, a, b, x0, tol, niter)

        img_interactiva = response['img_interactiva']
        script, div = components(img_interactiva)

        return render(request, 'm1.html', {'solucion'  : response['solucion'], 
                                            'iteraciones' : response['iteraciones'],
                                            'tabla': response['tabla'],
                                            'img_interactiva': img_interactiva,
                                            'script': script, 'div': div,
                                            'mensaje': response['mensaje']})
    else:
        return render(request, 'm1.html')

def m2(request):
    return render(request, 'm2.html')

def jacobi(request):
    pass

def gauss_seidel(request):
    pass

def sor(request):
    pass

def vandermonde(request):
    pass

def newtonInt(request):
    pass

def lagrange(request):
    pass