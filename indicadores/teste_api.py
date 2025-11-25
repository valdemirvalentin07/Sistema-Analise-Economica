from django.db.models import F, Sum, FloatField
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Indicador

@api_view(['GET'])
def indicadores_api(request):

    indicadores = Indicador.objects.all().order_by('-data_atualizacao')

    # Cálculo dos campos agregados
    soma_valor_total = indicadores.aggregate(
        total=Sum(F('valor') * F('quantidade'), output_field=FloatField())
    )['total'] or 0

    soma_lucro_total = indicadores.aggregate(
        total=Sum(F('valor') * F('quantidade') * F('percentual_lucro') / 100, output_field=FloatField())
    )['total'] or 0

    # Serialização manual com cálculos
    dados = []
    for i in indicadores:
        valor_total = float(i.valor) * i.quantidade
        lucro_total = valor_total * float(i.percentual_lucro) / 100

        dados.append({
            "id": i.id,
            "nome": i.nome,
            "categoria": i.categoria,
            "valor": float(i.valor),
            "quantidade": i.quantidade,
            "percentual_lucro": float(i.percentual_lucro),
            "valor_total": valor_total,
            "lucro_total": lucro_total,
            "data_atualizacao": i.data_atualizacao.strftime("%Y-%m-%d %H:%M:%S"),
        })

    return Response({
        "indicadores": dados,
        "soma_valor_total": soma_valor_total,
        "soma_lucro_total": soma_lucro_total
    })
