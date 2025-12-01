from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Indicador
import json

class IndicadoresViewsTestCase(TestCase):
    def setUp(self):
        # Criar usuário de teste
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')

        # Criar indicador de teste
        self.indicador = Indicador.objects.create(
            nome='Indicador Teste',
            categoria='Categoria A',
            valor=100.0,
            quantidade=5,
            percentual_lucro=20.0
        )

    def test_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('indicadores', response.context)

    def test_lista_indicadores(self):
        url = reverse('indicadores_lista')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('indicadores', response.context)
        self.assertIn('soma_valor_total', response.context)
        self.assertIn('soma_lucro_total', response.context)
        self.assertEqual(response.context['soma_valor_total'], 500.0)
        self.assertEqual(response.context['soma_lucro_total'], 100.0)

    def test_adicionar_indicador_get(self):
        url = reverse('adicionar_indicador')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_adicionar_indicador_post(self):
        url = reverse('adicionar_indicador')
        data = {
            'nome': 'Novo Indicador',
            'categoria': 'Categoria B',
            'valor': 50,
            'quantidade': 2,
            'percentual_lucro': 10
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Indicador.objects.filter(nome='Novo Indicador').exists())

    def test_editar_indicador_get(self):
        url = reverse('editar_indicador', args=[self.indicador.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_editar_indicador_post(self):
        url = reverse('editar_indicador', args=[self.indicador.id])
        data = {
            'nome': 'Indicador Editado',
            'categoria': self.indicador.categoria,
            'valor': self.indicador.valor,
            'quantidade': self.indicador.quantidade,
            'percentual_lucro': self.indicador.percentual_lucro
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.indicador.refresh_from_db()
        self.assertEqual(self.indicador.nome, 'Indicador Editado')

    def test_excluir_indicador_get(self):
        url = reverse('excluir_indicador', args=[self.indicador.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('indicador', response.context)

    def test_excluir_indicador_post(self):
        url = reverse('excluir_indicador', args=[self.indicador.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Indicador.objects.filter(id=self.indicador.id).exists())

    def test_indicadores_api(self):
        url = reverse('indicadores_api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertIn('indicadores', data)
        self.assertIn('soma_valor_total', data)
        self.assertIn('soma_lucro_total', data)

        self.assertEqual(data['soma_valor_total'], 500.0)
        self.assertEqual(data['soma_lucro_total'], 100.0)
        self.assertEqual(len(data['indicadores']), 1)
        self.assertEqual(data['indicadores'][0]['nome'], 'Indicador Teste')
