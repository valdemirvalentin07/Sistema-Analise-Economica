from django.apps import AppConfig


class IndicadoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'indicadores'
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'indicadores/home.html')
