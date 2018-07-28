from django_filters.rest_framework import FilterSet, NumberFilter, BooleanFilter
from api.models import Animal, Breed


class AnimalFilterSet(FilterSet):
    breed = NumberFilter(name='breed_field')
    is_castrated = BooleanFilter(method='is_castrated_filter')
    has_chip = BooleanFilter(method='has_chip_filter')

    def is_castrated_filter(self, queryset, name, value):
        return queryset.filter(medicalrecord__castrated=value)

    def has_chip_filter(self, queryset, name, value):
        return queryset.filter(medicalrecord__chip=value)

    class Meta:
        model = Animal
        fields = ('entity', 'size', 'sex')


class BreedFilterSet(FilterSet):
    species = NumberFilter(name='species_field')

    class Meta:
        model = Breed
        fields = ('name', )
