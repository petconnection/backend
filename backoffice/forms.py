# encoding=utf8
from django import forms
from api.models import Animal, Entity


class AnimalForm(forms.ModelForm):
    species = forms.CharField(required=True)
    class Meta:
        model = Animal
        fields = ('size', 'sex', 'bio')


class EntityForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = ('name', 'location')


