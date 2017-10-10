from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class LoginTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@test.org', '123')
        self.client = Client()


    def test_not_logged(self):
        response = self.client.get(reverse('backoffice_home'))
        self.assertRedirects(response, reverse('backoffice_login'))


    def test_view(self):
        response = self.client.get(reverse('backoffice_login'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.templates[0].name, 'backoffice/login.html')


    def test_login(self):
        response = self.client.post(reverse('backoffice_login'), {'username': 'testuser', 'password': '123'}, follow=True)
        self.assertRedirects(response, reverse('backoffice_home'))

