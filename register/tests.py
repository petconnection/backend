from django.test import TestCase, Client
from register.models import Token
from django.utils import timezone
from api.models import Entity


class RegisterTests(TestCase):
    def test_valid_token(self):
        token = Token()
        token.save()

        client = Client()
        response = client.get('/register/' + token.code + "/")
        self.assertEqual(response.status_code, 200)

    def test_expired_token(self):
        token = Token()
        token.expiry = timezone.now() - timezone.timedelta(hours=1)
        token.save()

        client = Client()
        response = client.get('/register/' + token.code + "/")
        self.assertTemplateUsed(response, 'error.html')

    def test_use_same_token_twice(self):
        token = Token()
        token.save()

        form_data = {
            "user_form-username": "RegisterTests_User",
            "user_form-password1": "Password123",
            "user_form-password2": "Password123",
            "entity_form-name": "RegisterTests Entity",
            "entity_form-location": "Test Location",
        }

        client = Client()
        client.post('/register/' + token.code + "/", form_data)
        entity_set = Entity.objects.filter(name=form_data["entity_form-name"])
        self.assertEqual(len(entity_set), 1, "Entity not registered properly")

        form_data["user_form-username"] += "_2"
        form_data["entity_form-name"] += "_2"

        client.post('/register/' + token.code + "/", form_data)
        entity_set = Entity.objects.filter(name=form_data["entity_form-name"])
        self.assertEqual(len(entity_set), 0, "Entity registered using an already used token")

    def test_register_user_using_invalid_token(self):
        form_data = {
            "user_form-username": "RegisterTests_InvalidToken",
            "user_form-password1": "Password123",
            "user_form-password2": "Password123",
            "entity_form-name": "RegisterTests InvalidToken",
            "entity_form-location": "Test Location",
        }

        client = Client()
        client.post('/register/abc/', form_data)
        entity_set = Entity.objects.filter(name=form_data["entity_form-name"])
        self.assertEqual(len(entity_set), 0, "Entity registered using an unexisting token")

