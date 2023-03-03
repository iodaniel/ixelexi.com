from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_authenticated_user(self):
        # Primero, intentamos acceder a una página que requiere autenticación sin estar autenticados.
        response = self.client.get(reverse('restricted'))
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('restricted'))

        # Luego, hacemos login con un usuario válido.
        self.client.login(username='testuser', password='testpass')

        # Ahora deberíamos poder acceder a la página restringida.
        response = self.client.get(reverse('restricted'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You are authenticated!")
