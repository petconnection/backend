from django.db import models


class BaseClass(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Entity(BaseClass):
    location = models.CharField(max_length=120)
    user = models.ForeignKey('auth.User')


class Species(BaseClass):
    pass


class Breed(BaseClass):
    species_field = models.ForeignKey(Species, on_delete=models.CASCADE)


class Animal(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
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
        breed = self.breed_field
        species = breed.species_field
        return "{} {}: {} {}".format(name, self.id, breed, species)

    @property
    def medical_record(self):
        return MedicalRecord.objects.get(animal=self.id)
    
    @property
    def species(self):
        return self.breed_field.species_field
        

class MedicalRecord(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, primary_key=True)
    vaccines = models.TextField(max_length=256, null=True, blank=True)
    castrated = models.NullBooleanField(null=True, blank=True, default=False)
    chip = models.NullBooleanField(null=True, blank=True, default=False)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}'s medical record".format(self.animal.name)


