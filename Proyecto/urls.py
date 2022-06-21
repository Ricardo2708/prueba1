"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sesion, name='sesion'),
    path('crear/',views.create, name='create'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name="logout"),
    path('inicio/',login_required(views.index), name='index'),
    path('chat/',login_required(views.chat), name='chat'),
    path('seccion_consulta/',login_required(views.seccion_consulta), name='seccion'),
    path('consulta/',login_required(views.consulta), name='consulta'),
    path('consultaA/',login_required(views.consultaA), name='consultaA'),
    path('consultaB/',login_required(views.consultaB), name='consultaB'),
    path('crear_casa/',login_required(views.crear_casa), name='crear_casa'),
    path('modificar/',login_required(views.modificar), name='modificar'),
    path('modificar_pdf/',login_required(views.modificar_pdf), name='modificar_pdf'),
    path('busquedaA/',login_required(views.busquedaA), name='busquedaA'),
    path('busquedaB/',login_required(views.busquedaB), name='busquedaB'),
    path('busquedaC/',login_required(views.busquedaC), name='busquedaC'),
    
]

handler404 = 'main.views.error_404'