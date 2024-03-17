from django.shortcuts import render
from django.http import HttpResponse
from .functions.biseccion import biseccion_func
# Create your views here.

import io 
import urllib, base64

def home(request):
    return render(request, 'index.html')
"""
def test(request):

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


        return render(request, 'test.html', {'sol'  : response['sol'], 
                                             'iter' : response['iter'],
                                             'tabla': response['tabla'],
                                             'img'  : img,
                                             'final': response['final']})
    else:
        return render(request, 'test.html')
"""
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
