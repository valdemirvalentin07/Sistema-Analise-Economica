from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UsuariosViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Criar usuário de teste
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_login_get(self):
        url = reverse('login')  # nome da URL de login
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Verifica se o formulário está presente
        self.assertContains(response, 'username')
        self.assertContains(response, 'password')

    def test_login_post_valid(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': '12345'}
        response = self.client.post(url, data)
        # Usuário válido deve redirecionar (status 302)
        self.assertEqual(response.status_code, 302)

    def test_login_post_invalid(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'wrongpass'}
        response = self.client.post(url, data)
        # Usuário inválido deve retornar status 200 e mostrar mensagem de erro
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Usuário ou senha incorretos.')

    def test_logout(self):
        self.client.login(username='testuser', password='12345')
        url = reverse('logout')
        response = self.client.get(url)
        # Redireciona após logout
        self.assertEqual(response.status_code, 302)
