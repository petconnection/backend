from django.test import TestCase, Client
from api.models import Animal, Entity, Species, Breed
from django.contrib.auth.models import User
from django.core.files.images import ImageFile
from json import loads


class AnimalTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('testuser', 'test@test.org', '123')
        e = Entity.objects.create(name='Aragonia', location='Palma', user=user)
        sp_dog = Species.objects.create(name='dog')
        sp_cat = Species.objects.create(name='cat') 
        br_dog = Breed.objects.create(name='husky', species_field=sp_dog)
        br_cat = Breed.objects.create(name='persa', species_field=sp_cat)
        animal = Animal.objects.create(
                name='Benji',
                entity=e,
                breed_field=br_dog)
        animal2 = Animal.objects.create(
                name='Oliver',
                entity=e,
                breed_field=br_cat)

    def test_get_animals(self):
        client = Client()
        response = client.get('api/animals')

        self.assertEqual(response.status_code, 200)
       
        data = loads(response.content)
       
        self.assertTrue(type(data['animals']) is list)

        for animal in data['animals']:
            self.__assert_animal(animal)
           
           
    def __assert_animal(self, animal):
        fields = ['entity', 'breed', 'specie']
        for f in fields:
            self.assertTure(f in animal)
            self.assertTrue(animal[f] is not None)


class EntityTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('testuser_entity', 'entity@test.org', '123')
        e = Entity.objects.create(name='Capsule Corp.', location='Molt enfora', user=user)

    def test_get_entities(self):
        client = Client()
        response = client.get('api/entities')
        self.assertEquals(response.status_code, 200)

        data = loads(response.content)

        for f in ['name','location']:
            self.assertTure(f in animal)
            self.assertTrue(animal[f] is not None)


