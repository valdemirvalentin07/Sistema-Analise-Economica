from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum, FloatField
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Indicador
from .forms import IndicadorForm


# === Views de CRUD ===

@login_required
def home_view(request):
    indicadores = Indicador.objects.all().order_by('-data_atualizacao')
    return render(request, 'indicadores/home.html', {'indicadores': indicadores})


@login_required
def lista_indicadores(request):
    indicadores = Indicador.objects.all().order_by('-data_atualizacao')

    # Soma total de valor (valor x quantidade)
    soma_valor_total = indicadores.aggregate(
        total=Sum(F('valor') * F('quantidade'), output_field=FloatField())
    )['total'] or 0

    # Soma total do lucro
    soma_lucro_total = indicadores.aggregate(
        total=Sum(
            F('valor') * F('quantidade') * F('percentual_lucro') / 100,
            output_field=FloatField()
        )
    )['total'] or 0

    context = {
        'indicadores': indicadores,
        'soma_valor_total': soma_valor_total,
        'soma_lucro_total': soma_lucro_total,
    }
    return render(request, 'indicadores/lista.html', context)


@login_required
def adicionar_indicador(request):
    if request.method == 'POST':
        form = IndicadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indicadores_lista')
    else:
        form = IndicadorForm()

    return render(request, 'indicadores/form.html', {
        'form': form,
        'titulo': 'Adicionar Indicador'
    })


@login_required
def editar_indicador(request, id):
    indicador = get_object_or_404(Indicador, id=id)

    if request.method == 'POST':
        form = IndicadorForm(request.POST, instance=indicador)
        if form.is_valid():
            form.save()
            return redirect('indicadores_lista')
    else:
        form = IndicadorForm(instance=indicador)

    return render(request, 'indicadores/form.html', {
        'form': form,
        'titulo': 'Editar Indicador'
    })


@login_required
def excluir_indicador(request, id):
    indicador = get_object_or_404(Indicador, id=id)

    if request.method == 'POST':
        indicador.delete()
        return redirect('indicadores_lista')

    return render(request, 'indicadores/confirm_delete.html', {
        'indicador': indicador
    })


# === API para consumo no Power BI ===
@api_view(['GET'])
def indicadores_api(request):
    indicadores = Indicador.objects.all().order_by('-data_atualizacao')

    data = []
    soma_valor_total = 0
    soma_lucro_total = 0

    for i in indicadores:
        valor_total = float(i.valor) * i.quantidade
        lucro_total = valor_total * float(i.percentual_lucro) / 100

        soma_valor_total += valor_total
        soma_lucro_total += lucro_total

        data.append({
            'id': i.id,
            'nome': i.nome,
            'categoria': i.categoria,
            'valor': float(i.valor),
            'quantidade': i.quantidade,
            'percentual_lucro': float(i.percentual_lucro),
            'valor_total': valor_total,
            'lucro_total': lucro_total,
            'data_atualizacao': i.data_atualizacao.strftime('%Y-%m-%d %H:%M:%S')
        })

    return Response({
        'indicadores': data,
        'soma_valor_total': soma_valor_total,
        'soma_lucro_total': soma_lucro_total
    })
