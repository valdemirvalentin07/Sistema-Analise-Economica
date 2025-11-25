from django import forms
from .models import Indicador

class IndicadorForm(forms.ModelForm):
    class Meta:
        model = Indicador
        fields = ['nome', 'categoria', 'valor', 'quantidade', 'percentual_lucro']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do indicador'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoria'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'percentual_lucro': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '100'}),
        }
