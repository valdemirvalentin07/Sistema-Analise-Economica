"""
URL configuration for economia project.
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect, render
from indicadores import views

# Certifique-se de criar a view home_view se ainda não existir:
# indicadores/views.py
# def home_view(request):
#     return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('indicadores/', include('indicadores.urls')),
    

    # Ajuste: usamos uma view existente ou criamos a home_view
    path('home/', views.home_view, name='home'),

    # Redireciona a raiz para login
    path('', lambda request: redirect('/usuarios/login/')),
]
