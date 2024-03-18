from django.shortcuts import render
from django.http import HttpResponse
from .functions.biseccion import biseccion_func
from .functions.reglafalsa import reglafalsa_func
from .functions.puntofijo import puntofijo_func
# Create your views here.

import matplotlib.pyplot as plt
import matplotlib
import io 
import urllib, base64
from bokeh.embed import components

def home(request):
    return render(request, 'index.html')

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

        response = puntofijo_func(funcion, a, b, tol, niter)

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
