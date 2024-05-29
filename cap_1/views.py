import json
from django.shortcuts import render
from django.http import HttpResponse
import os

# ================Part 1================
from .functions.busquedas import busquedas_func
from .functions.biseccion import biseccion_func
from .functions.reglafalsa import reglafalsa_func
from .functions.puntofijo import puntofijo_func
from .functions.newton import newton_func
from .functions.secante import secante_func
from .functions.m1 import m1_func
from .functions.biseccion import iteracion

# ================Part 2================
from .functions.jacobi import MatJacobi
from .functions.gauss_seidel import Gauss_seidel
from .functions.sor import SOR

# ================Part 3================
from .functions.vander import Vandermonde
from .functions.newtonInt import NewtonInt
from .functions.lagrange import Lagrange
# Create your views here.

import matplotlib.pyplot as plt
import matplotlib
import io 
import urllib, base64
from bokeh.embed import components


def home(request):
    return render(request, 'index.html')

# ================================Part 1================================
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
        error_type = request.POST['error_type']
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])
        export_txt = request.POST.get('export-txt')

        response = biseccion_func(funcion, a, b,error_type, tol, niter)

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

        if export_txt == 'on':
            directory = os.path.abspath('../Pruebas')
            print(f"Directory: {directory}")  # Print the directory
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory, 'biseccion_results.txt')
            print(f"Filepath: {filepath}")  # Print the filepath
            with open(filepath, 'w') as f:
                for key, value in response.items():
                    if key == 'tabla':
                        f.write(f'{key}:\n')
                        for item in value:
                            f.write(f'i={item.i}, x={item.x}, fx={item.fx}, err={item.err}\n')
                    elif key == 'img_interactiva':
            # No imprimimos 'img_interactiva' ya que no es legible en texto
                        continue
                    else:
                        f.write(f'{key}: {value}\n')

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
        error_type = request.POST['error_type']
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])
        export_txt = request.POST.get('export-txt')

        response = reglafalsa_func(funcion, a, b,error_type, tol, niter)
        img_interactiva = response['img_interactiva']
        script, div = components(img_interactiva)

        if export_txt == 'on':
            directory = os.path.abspath('../Pruebas')
            print(f"Directory: {directory}")  # Print the directory
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory, 'reglafalsa_results.txt')
            print(f"Filepath: {filepath}")  # Print the filepath
            with open(filepath, 'w') as f:
                for key, value in response.items():
                    if key == 'tabla':
                        f.write(f'{key}:\n')
                        for item in value:
                            f.write(f'i={item.i}, x={item.x}, fx={item.fx}, err={item.err}\n')
                    elif key == 'img_interactiva':
            # No imprimimos 'img_interactiva' ya que no es legible en texto
                        continue
                    else:
                        f.write(f'{key}: {value}\n')
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
        error_type = request.POST['error_type']
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])
        export_txt = request.POST.get('export-txt')

        response = puntofijo_func(funcion, funcion_g, x0,error_type, tol, niter)

        img_interactiva = response['img_interactiva']
        script, div = components(img_interactiva)

        if export_txt == 'on':
            directory = os.path.abspath('../Pruebas')
            print(f"Directory: {directory}")  # Print the directory
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory, 'puntofijo_results.txt')
            print(f"Filepath: {filepath}")  # Print the filepath
            with open(filepath, 'w') as f:
                for key, value in response.items():
                    if key == 'tabla':
                        f.write(f'{key}:\n')
                        for item in value:
                            f.write(f'i={item.i}, x={item.x}, fx={item.fx}, err={item.err}\n')
                    elif key == 'img_interactiva':
            # No imprimimos 'img_interactiva' ya que no es legible en texto
                        continue
                    else:
                        f.write(f'{key}: {value}\n')
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
        error_type = request.POST['error_type']
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])
        export_txt = request.POST.get('export-txt')

        response = newton_func(funcion, x0,error_type, tol, niter)

        img_interactiva = response['img_interactiva']
        script, div = components(img_interactiva)

        if export_txt == 'on':
            directory = os.path.abspath('../Pruebas')
            print(f"Directory: {directory}")  # Print the directory
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory, 'newton_results.txt')
            print(f"Filepath: {filepath}")  # Print the filepath
            with open(filepath, 'w') as f:
                for key, value in response.items():
                    if key == 'tabla':
                        f.write(f'{key}:\n')
                        for item in value:
                            f.write(f'i={item.i}, x={item.x}, fx={item.fx}, err={item.err}\n')
                    elif key == 'img_interactiva':
            # No imprimimos 'img_interactiva' ya que no es legible en texto
                        continue
                    else:
                        f.write(f'{key}: {value}\n')

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
        error_type = request.POST['error_type']
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])
        export_txt = request.POST.get('export-txt')

        response = secante_func(funcion, x0, x1,error_type, tol, niter)

        img_interactiva = response['img_interactiva']
        try:
            script, div = components(img_interactiva)
        except:
            script, div = None, None

        if export_txt == 'on':
            directory = os.path.abspath('../Pruebas')
            print(f"Directory: {directory}")  # Print the directory
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory, 'secante_results.txt')
            print(f"Filepath: {filepath}")  # Print the filepath
            with open(filepath, 'w') as f:
                for key, value in response.items():
                    if key == 'tabla':
                        f.write(f'{key}:\n')
                        for item in value:
                            f.write(f'i={item.i}, x={item.x}, fx={item.fx}, err={item.err}\n')
                    elif key == 'img_interactiva':
            # No imprimimos 'img_interactiva' ya que no es legible en texto
                        continue
                    else:
                        f.write(f'{key}: {value}\n')
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
        m = float(request.POST['m'])
        error_type = request.POST['error_type']
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])
        export_txt = request.POST.get('export-txt')

        response = m1_func(funcion, m, x0,error_type, tol, niter)

        img_interactiva = response['img_interactiva']
        script, div = components(img_interactiva)

        if export_txt == 'on':
            directory = os.path.abspath('../Pruebas')
            print(f"Directory: {directory}")  # Print the directory
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory, 'm1_results.txt')
            print(f"Filepath: {filepath}")  # Print the filepath
            with open(filepath, 'w') as f:
                for key, value in response.items():
                    if key == 'tabla':
                        f.write(f'{key}:\n')
                        for item in value:
                            f.write(f'i={item.i}, x={item.x}, fx={item.fx}, err={item.err}\n')
                    elif key == 'img_interactiva':
            # No imprimimos 'img_interactiva' ya que no es legible en texto
                        continue
                    else:
                        f.write(f'{key}: {value}\n')

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


# ================================Part 2================================
def jacobi(request):
    if request.method == 'POST':
        x0 = request.POST['x0']
        A = request.POST['A']
        b = request.POST['b']
        Tol = request.POST['tol']
        niter = request.POST['niter']

        s = MatJacobi(x0, A, b, Tol, niter)
        #print({'solucion': s['solucion'],
       #'iteraciones': s['iteraciones'],
       #'tabla': s['tabla'],
       #'mensaje': s['mensaje']})

        return render(request, 'jacobi.html', {'solucion': s['solucion'],
                                                'iteraciones': s['iteraciones'],
                                                'tabla': s['tabla'],
                                                'mensaje': s['mensaje']})

    else:
        return render(request, 'jacobi.html')


def gauss_seidel(request):
    if request.method == 'POST':
        x0 = request.POST['x0']
        A = request.POST['A']
        b = request.POST['b']
        Tol = request.POST['tol']
        niter = request.POST['niter']

        s = Gauss_seidel(x0, A, b, Tol, niter)

        return render(request, 'gauss_seidel.html', {'solucion': s['solucion'],
                                                'iteraciones': s['iteraciones'],
                                                'tabla': s['tabla'],
                                                'mensaje': s['mensaje']})

    else:
        return render(request, 'gauss_seidel.html')


def sor(request):
    if request.method == 'POST':
        x0 = request.POST['x0']
        A = request.POST['A']
        b = request.POST['b']
        Tol = request.POST['tol']
        niter = request.POST['niter']
        w = request.POST['w']

        s = SOR(x0, A, b, Tol, niter, w)

        return render(request, 'sor.html', {'solucion': s['solucion'],
                                                'iteraciones': s['iteraciones'],
                                                'tabla': s['tabla'],
                                                'mensaje': s['mensaje']})

    else:
        return render(request, 'sor.html')


# ================================Part 3================================
def vandermonde(request):
    if request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']

        s = Vandermonde(x, y)

        img_interactiva = s['img_interactiva']
        script, div = components(img_interactiva)

        return render(request, 'lagrange.html', {'tabla': s['tabla'],
                                                 'script': script, 'div': div,
                                                    'funcion': s['funcion'],
                                                    'mensaje': s['mensaje']})

    else:
        return render(request, 'lagrange.html')


def newtonInt(request):
    if request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']

        s = NewtonInt(x, y)
        img_interactiva = s['img_interactiva']
        script, div = components(img_interactiva)

        return render(request, 'newtonint.html', {'tabla': s['tabla'],
                                                    'script': script, 'div': div,
                                                    'funcion': s['funcion'],
                                                    'mensaje': s['mensaje']})

    else:
        return render(request, 'newtonint.html')


def lagrange(request):
    if request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']

        s = Lagrange(x, y)
        img_interactiva = s['img_interactiva']
        script, div = components(img_interactiva)

        return render(request, 'lagrange.html', {'tabla': s['tabla'],
                                                    'script': script, 'div': div,
                                                    'funcion': s['funcion'],
                                                    'mensaje': s['mensaje']})

    else:
        return render(request, 'lagrange.html')

def spline_lineal(request):
    return render(request, 'spline_lineal.html')

def spline_cuadratico(request):
    return render(request, 'spline_cuadratico.html')

def spline_cubico(request):
    return render(request, 'spline_cubico.html')