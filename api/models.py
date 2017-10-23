from django.db import models
from django.core.validators import RegexValidator


class BaseClass(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Entity(BaseClass):
    location = models.CharField(max_length=120)
    user = models.ForeignKey('auth.User')
    email = models.EmailField(max_length=60)
    phone_regex = RegexValidator(regex="[0-9]{9}", message="Not a valid phone number", code=400)
    phone = models.CharField(max_length=9, validators=[phone_regex])


class Species(BaseClass):
    pass


class Breed(BaseClass):
    species_field = models.ForeignKey(Species, on_delete=models.CASCADE)


class Animal(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    weigth = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    SIZES = (
            ('S', 'small'),
            ('M', 'medium'),
            ('B', 'big')
            )
    size = models.CharField(max_length=2, choices=SIZES, default='M')
    SEX = (
            ('M', 'male'),
            ('F', 'female')
            )
    sex = models.CharField(max_length=2, choices=SEX, default='M')
    registration = models.DateTimeField(auto_now_add=True)
    breed_field = models.ForeignKey(Breed, on_delete=models.CASCADE)
    pic = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        name = self.name if self.name else ""
        breed_field = self.breed_field
        species_field = breed_field.species_field
        return "{name} {animal_id}: {breed} {species}".format(name=name, animal_id=self.id, breed=breed_field, species=species_field)


class MedicalRecord(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, primary_key=True)
    vaccines = models.TextField(max_length=256, null=True, blank=True)
    castrated = models.NullBooleanField(null=True, blank=True, default=False)
    chip = models.NullBooleanField(null=True, blank=True, default=False)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}'s medical record".format(self.animal.name)


