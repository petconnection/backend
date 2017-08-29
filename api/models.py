from django.db import models


class Entity(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=120)
    user = models.ForeignKey('auth.User')

    def __str__(self):
        return self.name


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
    classification_1 = models.CharField(max_length=30)
    classification_2 = models.CharField(max_length=30, null=True, blank=True)
    pic = models.ImageField()
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class MedicalRecord(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    vaccines = models.TextField(max_length=256, null=True, blank=True)
    castrated = models.NullBooleanField(null=True, blank=True, default=False)
    chip = models.NullBooleanField(null=True, blank=True, default=False)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}'s medical record".format(self.animal.name)


