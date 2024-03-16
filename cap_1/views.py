from django.shortcuts import render
from django.http import HttpResponse
from .functions.biseccion import biseccion_func
# Create your views here.

def home(request):
    return render(request, 'index.html')


def test(request):

    if request.method == 'POST':
        funcion = request.POST['funcion']
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])

        response = biseccion_func(funcion, a, b, tol, niter)

        return render(request, 'test.html', {'sol'  : response['sol'], 
                                             'iter' : response['iter'],
                                             'tabla': response['tabla'],
                                             'img'  : response['img'],
                                             'final': response['final']})
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

        return render(request, 'biseccion.html', {'sol'  : response['sol'], 
                                                  'iter' : response['iter'], 
                                                  'tabla': response['tabla'], 
                                                  'final': response['final']})
    else:
        return render(request, 'biseccion.html')
