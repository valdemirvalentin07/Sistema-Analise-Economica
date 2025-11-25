from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_indicadores, name='indicadores_lista'),
    path('adicionar/', views.adicionar_indicador, name='adicionar_indicador'),
    path('editar/<int:id>/', views.editar_indicador, name='editar_indicador'),
    path('excluir/<int:id>/', views.excluir_indicador, name='excluir_indicador'),
    path('api/', views.indicadores_api, name='indicadores_api'),  # rota da API
]
