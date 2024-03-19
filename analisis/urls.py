"""
URL configuration for analisis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cap_1 import views as cap_1_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cap_1_views.home, name='index'),
    path('maquina', cap_1_views.maquina, name='maquina')
    path('busquedas', cap_1_views.busquedas, name='busquedas'),
    path('biseccion', cap_1_views.biseccion, name='biseccion'),
    path('reglafalsa', cap_1_views.reglafalsa, name='reglafalsa'),
    path('puntofijo', cap_1_views.puntofijo, name='puntofijo'),
    path('newton', cap_1_views.newton, name='newton'),
    path('secante', cap_1_views.secante, name='secante'),
    path('m1', cap_1_views.m1, name='m1'),
    path('m2', cap_1_views.m1, name='m2'),
]
