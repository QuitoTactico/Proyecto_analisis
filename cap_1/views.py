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
from .functions.splineLineal import spline_lineal
from .functions.splineCuadratico import spline_cuadratico
from .functions.splineCubico import spline_cubico

import matplotlib.pyplot as plt
import matplotlib
import io 
import urllib, base64
from bokeh.embed import components

def export_to_txt(filepath, response):
    filepath = f'{filepath}_results.txt'
    directory = os.path.abspath('Pruebas')
    print(f"Directory: {directory}")  
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filepath)
    print(f"Filepath: {filepath}")  
    with open(filepath, 'w') as f:
        for key, value in response.items():
            if key == 'tabla':
                f.write(f'{key}:\n')
                for item in value:
                    f.write(f'i={item.i}, x={item.x}, fx={item.fx}\n, err={item.err}')
            elif key == 'img_interactiva':
    # No imprimimos 'img_interactiva' ya que no es legible en texto
                continue
            else:
                f.write(f'{key}: {value}\n')

def home(request):
    return render(request, 'index.html')

# ================================Part 1================================
def busquedas(request):
    if request.method == 'POST':
        funcion = request.POST['funcion']
        x0 = float(request.POST['x0'])
        dx = float(request.POST['dx'])
        niter = int(request.POST['niter'])
        export_txt = request.POST.get('export-txt')

        response = busquedas_func(funcion, x0, dx, niter)

        try:
            img_interactiva = response['img_interactiva']
            script, div = components(img_interactiva)

            if export_txt == 'on':
                directory = os.path.abspath('Pruebas')
                print(f"Directory: {directory}")  
                if not os.path.exists(directory):
                    os.makedirs(directory)
                filepath = os.path.join(directory, 'busquedas_results.txt')
                print(f"Filepath: {filepath}")  
                with open(filepath, 'w') as f:
                    for key, value in response.items():
                        if key == 'tabla':
                            f.write(f'{key}:\n')
                            for item in value:
                                f.write(f'i={item.i}, x={item.x}, fx={item.fx}\n')
                        elif key == 'img_interactiva':
                # No imprimimos 'img_interactiva' ya que no es legible en texto
                            continue
                        else:
                            f.write(f'{key}: {value}\n')

            return render(request, 'busquedas.html', {'solucion'  : response['solucion'], 
                                                'iteraciones' : response['iteraciones'],
                                                'tabla': response['tabla'],
                                                'img_interactiva': img_interactiva,
                                                'script': script, 'div': div,
                                                'mensaje': response['mensaje']})
        except:
            return render(request, 'busquedas.html', {'mensaje': response['mensaje']})
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
        try:
            img_interactiva = response['img_interactiva']
            script, div = components(img_interactiva)

            if export_txt == 'on':
                export_to_txt('biseccion', response)

            return render(request, 'biseccion.html', {'solucion'  : response['solucion'], 
                                                'iteraciones' : response['iteraciones'],
                                                'tabla': response['tabla'],
                                                'img_interactiva': img_interactiva,
                                                'script': script, 'div': div,
                                                'mensaje': response['mensaje']})
        except:
            return render(request, 'biseccion.html', {'mensaje': response['mensaje']})
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

        try:
            img_interactiva = response['img_interactiva']
            script, div = components(img_interactiva)

            if export_txt == 'on':
                export_to_txt('reglafalsa', response)
            return render(request, 'reglafalsa.html', {'solucion'  : response['solucion'], 
                                                'iteraciones' : response['iteraciones'],
                                                'tabla': response['tabla'],
                                                'img_interactiva': img_interactiva,
                                                'script': script, 'div': div,
                                                'mensaje': response['mensaje']})
        except:
            return render(request, 'reglafalsa.html', {'mensaje': response['mensaje']})
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

        try:
            img_interactiva = response['img_interactiva']
            script, div = components(img_interactiva)

            if export_txt == 'on':
                export_to_txt('puntofijo', response)
            return render(request, 'puntofijo.html', {'solucion'  : response['solucion'], 
                                                'iteraciones' : response['iteraciones'],
                                                'tabla': response['tabla'],
                                                'img_interactiva': img_interactiva,
                                                'script': script, 'div': div,
                                                'mensaje': response['mensaje']})
        except:
            return render(request, 'puntofijo.html', {'mensaje': response['mensaje']})
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

        try:
            img_interactiva = response['img_interactiva']
            script, div = components(img_interactiva)

            if export_txt == 'on':
                export_to_txt('newton', response)

            return render(request, 'newton.html', {'solucion'  : response['solucion'], 
                                                'iteraciones' : response['iteraciones'],
                                                'tabla': response['tabla'],
                                                'img_interactiva': img_interactiva,
                                                'script': script, 'div': div,
                                                'mensaje': response['mensaje']})
        except:
            return render(request, 'newton.html', {'mensaje': response['mensaje']})
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

            if export_txt == 'on':
                export_to_txt('secante', response)
            return render(request, 'secante.html', {'solucion'  : response['solucion'], 
                                                'iteraciones' : response['iteraciones'],
                                                'tabla': response['tabla'],
                                                'img_interactiva': img_interactiva,
                                                'script': script, 'div': div,
                                                'mensaje': response['mensaje']})
        except:
            return render(request, 'secante.html', {'mensaje': response['mensaje']})
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

        try:
            img_interactiva = response['img_interactiva']
            script, div = components(img_interactiva)

            if export_txt == 'on':
                export_to_txt('m1', response)

            return render(request, 'm1.html', {'solucion'  : response['solucion'], 
                                                'iteraciones' : response['iteraciones'],
                                                'tabla': response['tabla'],
                                                'img_interactiva': img_interactiva,
                                                'script': script, 'div': div,
                                                'mensaje': response['mensaje']})
        except:
            return render(request, 'm1.html', {'mensaje': response['mensaje']})
    else:
        return render(request, 'm1.html')

# ================================Part 2================================
def jacobi(request):
    if request.method == 'POST':
        x0 = request.POST['x0']
        A = request.POST['A']
        b = request.POST['b']
        Tol = request.POST['tol']
        niter = request.POST['niter']
        export_txt = request.POST.get('export-txt')

        s = MatJacobi(x0, A, b, Tol, niter)
        #print({'solucion': s['solucion'],
       #'iteraciones': s['iteraciones'],
       #'tabla': s['tabla'],
       #'mensaje': s['mensaje']})
        if export_txt == 'on':
            directory = os.path.abspath('Pruebas')
            print(f"Directory: {directory}")  
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory, 'jacobi_results.txt')
            print(f"Filepath: {filepath}")  
            with open(filepath, 'w') as f:
                for key, value in s.items():
                    if key == 'tabla':
                        f.write(f'{key}:\n')
                        for item in value:
                            f.write(f'c={item.c}, error={item.error}, x0={item.x0}\n')
                    elif key == 'img_interactiva':
            # No imprimimos 'img_interactiva' ya que no es legible en texto
                        continue
                    else:
                        f.write(f'{key}: {value}\n')

        try:
            return render(request, 'jacobi.html', {'solucion': s['solucion'],
                                                    'iteraciones': s['iteraciones'],
                                                    'tabla': s['tabla'],
                                                    'mensaje': s['mensaje']})
        except:
            return render(request, 'jacobi.html', {'mensaje': s['mensaje']})

    return render(request, 'jacobi.html')


def gauss_seidel(request):
    if request.method == 'POST':
        x0 = request.POST['x0']
        A = request.POST['A']
        b = request.POST['b']
        Tol = request.POST['tol']
        niter = request.POST['niter']
        export_txt = request.POST.get('export-txt')

        s = Gauss_seidel(x0, A, b, Tol, niter)

        if export_txt == 'on':
            directory = os.path.abspath('Pruebas')
            print(f"Directory: {directory}")  
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory, 'gauss_seidel_results.txt')
            print(f"Filepath: {filepath}")  
            with open(filepath, 'w') as f:
                for key, value in s.items():
                    if key == 'tabla':
                        f.write(f'{key}:\n')
                        for item in value:
                            f.write(f'c={item.c}, error={item.error}, x0={item.x0}\n')
                    elif key == 'img_interactiva':
            # No imprimimos 'img_interactiva' ya que no es legible en texto
                        continue
                    else:
                        f.write(f'{key}: {value}\n')

        try:
            return render(request, 'gauss_seidel.html', {'solucion': s['solucion'],
                                                    'iteraciones': s['iteraciones'],
                                                    'tabla': s['tabla'],
                                                    'mensaje': s['mensaje']})
        except:
            return render(request, 'gauss_seidel.html', {'mensaje': s['mensaje']})

    return render(request, 'gauss_seidel.html')


def sor(request):
    if request.method == 'POST':
        x0 = request.POST['x0']
        A = request.POST['A']
        b = request.POST['b']
        Tol = request.POST['tol']
        niter = request.POST['niter']
        w = request.POST['w']
        export_txt = request.POST.get('export-txt')

        s = SOR(x0, A, b, Tol, niter, w)

        if export_txt == 'on':
            directory = os.path.abspath('Pruebas')
            print(f"Directory: {directory}")  
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory, 'sor_results.txt')
            print(f"Filepath: {filepath}")  
            with open(filepath, 'w') as f:
                for key, value in s.items():
                    if key == 'tabla':
                        f.write(f'{key}:\n')
                        for item in value:
                            f.write(f'c={item.c}, error={item.error}, x0={item.x0}\n')
                    elif key == 'img_interactiva':
            # No imprimimos 'img_interactiva' ya que no es legible en texto
                        continue
                    else:
                        f.write(f'{key}: {value}\n')

        try:
            return render(request, 'sor.html', {'solucion': s['solucion'],
                                                    'iteraciones': s['iteraciones'],
                                                    'tabla': s['tabla'],
                                                    'mensaje': s['mensaje']})
        except:
            return render(request, 'sor.html', {'mensaje': s['mensaje']})

    return render(request, 'sor.html')


# ================================Part 3================================
def vandermonde(request):
    if request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']
        export_txt = request.POST.get('export-txt')

        s = Vandermonde(x, y)

        img_interactiva = s['img_interactiva']
        script, div = components(img_interactiva)

        
        if export_txt == 'on':
            directory = os.path.abspath('Pruebas')
            print(f"Directory: {directory}")  
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory, 'vander_results.txt')
            print(f"Filepath: {filepath}")  
            with open(filepath, 'w') as f:
                f.write(f"funcion: {s['funcion']}\n")
                f.write(f"mensaje: {s['mensaje']}\n")
        try:
            return render(request, 'vandermonde.html', {'tabla': s['tabla'],
                                                    'script': script, 'div': div,
                                                        'funcion': s['funcion'],
                                                        'mensaje': s['mensaje']})
        except:
            return render(request, 'vandermonde.html', {'mensaje': s['mensaje']})

    return render(request, 'vandermonde.html')


def newtonInt(request):
    if request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']
        export_txt = request.POST.get('export-txt')

        s = NewtonInt(x, y)
        img_interactiva = s['img_interactiva']
        script, div = components(img_interactiva)

        if export_txt == 'on':
            directory = os.path.abspath('Pruebas')
            print(f"Directory: {directory}")  
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory, 'newton_results.txt')
            print(f"Filepath: {filepath}")  
            with open(filepath, 'w') as f:
                f.write(f"funcion: {s['funcion']}\n")
                f.write(f"mensaje: {s['mensaje']}\n")
                if 'tabla' in s:
                    f.write('tabla:\n')
                    for row in s['tabla']:
                        f.write('\t'.join(map(str, row)) + '\n')

        try:
            return render(request, 'newtonint.html', {'tabla': s['tabla'],
                                                        'script': script, 'div': div,
                                                        'funcion': s['funcion'],
                                                        'mensaje': s['mensaje']})
        except:
            return render(request, 'newtonint.html', {'mensaje': s['mensaje']})

    return render(request, 'newtonint.html')


def lagrange(request):
    if request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']
        export_txt = request.POST.get('export-txt')

        s = Lagrange(x, y)
        img_interactiva = s['img_interactiva']
        script, div = components(img_interactiva)

        if export_txt == 'on':
            directory = os.path.abspath('Pruebas')
            print(f"Directory: {directory}")  
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory, 'lagrange_results.txt')
            print(f"Filepath: {filepath}")  
            with open(filepath, 'w') as f:
                f.write(f"funcion: {s['funcion']}\n")
                f.write(f"mensaje: {s['mensaje']}\n")
                if 'tabla' in s:
                    f.write('tabla:\n')
                    for item in s['tabla']:
                        f.write(str(item) + '\n')

        try:
            return render(request, 'lagrange.html', {'tabla': s['tabla'],
                                                        'script': script, 'div': div,
                                                        'funcion': s['funcion'],
                                                        'mensaje': s['mensaje']})
        except:
            return render(request, 'lagrange.html', {'mensaje': s['mensaje']})

    return render(request, 'lagrange.html')

def splinelineal(request):
    if request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']
        export_txt = request.POST.get('export-txt')

        tabla, img_interactiva = spline_lineal(x, y)

        try:
            return render(request, 'spline_lineal.html', {'solucion': tabla['mensaje']})
        except:

            if export_txt == 'on':
                directory = os.path.abspath('Pruebas')
                print(f"Directory: {directory}")  
                if not os.path.exists(directory):
                    os.makedirs(directory)
                filepath = os.path.join(directory, 'splinelineal.txt')
                print(f"Filepath: {filepath}")  
                with open(filepath, 'w') as f:
                    for item in tabla:
                        f.write(str(item.function_str) + '\n')

            script, div = components(img_interactiva)
            return render(request, 'spline_lineal.html', {'solucion': tabla,
                                                          'script': script, 'div': div,})

    return render(request, 'spline_lineal.html')

def splinecuadratico(request):
    if request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']
        export_txt = request.POST.get('export-txt')

        tabla, img_interactiva = spline_cuadratico(x, y)

        try:
            return render(request, 'spline_cuadratico.html', {'error': tabla['mensaje']})
        except:
            if export_txt == 'on':
                directory = os.path.abspath('Pruebas')
                print(f"Directory: {directory}")  
                if not os.path.exists(directory):
                    os.makedirs(directory)
                filepath = os.path.join(directory, 'splinecuadratico.txt')
                print(f"Filepath: {filepath}")  
                with open(filepath, 'w') as f:
                    for item in tabla:
                        f.write(str(item.function_str) + '\n')

            script, div = components(img_interactiva)
            return render(request, 'spline_cuadratico.html', {'tabla': tabla,
                                                              'script': script, 'div': div})

    return render(request, 'spline_cuadratico.html')

def splinecubico(request):
    if request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']
        export_txt = request.POST.get('export-txt')

        tabla, img_interactiva = spline_cubico(x, y)

        try:
            return render(request, 'spline_cubico.html', {'solucion': tabla['mensaje']})
        except:
            if export_txt == 'on':
                directory = os.path.abspath('Pruebas')
                print(f"Directory: {directory}")  
                if not os.path.exists(directory):
                    os.makedirs(directory)
                filepath = os.path.join(directory, 'splinecubico.txt')
                print(f"Filepath: {filepath}")  
                with open(filepath, 'w') as f:
                    for item in tabla:
                        f.write(str(item.function_str) + '\n')

            script, div = components(img_interactiva)
            return render(request, 'spline_cubico.html', {'solucion': tabla,
                                                          'script': script, 'div': div,})

    return render(request, 'spline_cubico.html')