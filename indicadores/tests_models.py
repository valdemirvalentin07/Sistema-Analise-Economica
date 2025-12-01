
from django.test import TestCase
from .models import Indicador
from decimal import Decimal

class IndicadorModelTestCase(TestCase):
    def setUp(self):
        self.indicador = Indicador.objects.create(
            nome='Indicador Teste',
            categoria='Categoria A',
            valor=Decimal('100.00'),
            quantidade=5,
            percentual_lucro=Decimal('20.00')
        )

    def test_str(self):
        self.assertEqual(str(self.indicador), "Indicador Teste (Categoria A)")

    def test_valor_total_property(self):
        self.assertEqual(self.indicador.valor_total, Decimal('500.00'))

    def test_lucro_total_property(self):
        self.assertEqual(self.indicador.lucro_total, Decimal('100.00'))
