from django_filters.rest_framework import FilterSet, NumberFilter
from api.models import Animal


class AnimalFilterSet(FilterSet):
    breed = NumberFilter(name='breed_field')

    class Meta:
        model = Animal
        fields = ('entity', 'size', 'sex')
