from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    error = None  # variável para mensagens de erro

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # ajuste para sua página inicial
        else:
            error = "Usuário ou senha incorretos."  # mensagem exibida no template

    return render(request, 'usuarios/login.html', {'error': error})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
