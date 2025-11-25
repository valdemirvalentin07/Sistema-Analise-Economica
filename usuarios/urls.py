from django.urls import path
from . import views  # importa as views do app usuarios

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
