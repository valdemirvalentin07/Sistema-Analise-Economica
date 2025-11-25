from rest_framework import serializers
from .models import Indicador

class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        fields = [
            'id',
            'nome',
            'categoria',
            'valor',
            'quantidade',
            'percentual_lucro'
        ]
