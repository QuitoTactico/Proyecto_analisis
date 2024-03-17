from django.shortcuts import render
from django.http import HttpResponse
from .functions.biseccion import biseccion_func
# Create your views here.

import matplotlib.pyplot as plt
import matplotlib
import io 
import urllib, base64
from bokeh.embed import components
from bokeh.plotting import show

def home(request):
    return render(request, 'index.html')


def test(request):

    if request.method == 'POST':
        matplotlib.use('Agg')

        funcion = request.POST['funcion']
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])

        response = biseccion_func(funcion, a, b, tol, niter)

        img = response['img']
        #img = io.BytesIO(urllib.parse.unquote(img).encode('utf-8'))
        #img = base64.b64encode(img.getvalue()).decode()

        buffer = io.BytesIO()
        img.save(buffer)
        #plt.savefig(buffer, format='png') 
        buffer.seek(0) 
        #img_interactiva.close() 
        
        # Convertir la gráfica a base64 
        image_png = buffer.getvalue() 
        buffer.close() 
        img = base64.b64encode(image_png) 
        img = img.decode('utf-8') 

        # lo épico
        img_interactiva = response['img_interactiva']
        script, div = components(img_interactiva)
        show(img_interactiva)
        #print(script, div)

        return render(request, 'test.html', {'solucion'  : response['solucion'], 
                                             'iteraciones' : response['iteraciones'],
                                             'tabla': response['tabla'],
                                             'img'  : img,
                                             'img_interactiva': img_interactiva,
                                             'script': script, 'div': div,
                                             'mensaje': response['mensaje']})
    else:
        return render(request, 'test.html')

def biseccion(request):

    if request.method == 'POST':
        funcion = request.POST['funcion']
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])

        response = biseccion_func(funcion, a, b, tol, niter)

        img = response['img']
        #img = io.BytesIO(urllib.parse.unquote(img).encode('utf-8'))
        #img = base64.b64encode(img.getvalue()).decode()


        return render(request, 'biseccion.html', {'sol'  : response['sol'], 
                                             'iter' : response['iter'],
                                             'tabla': response['tabla'],
                                             'img'  : img,
                                             'final': response['final']})
    else:
        return render(request, 'biseccion.html')
