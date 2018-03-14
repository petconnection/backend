from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api import serializers
from api.filters import AnimalFilterSet
from api.models import Animal, Entity, MedicalRecord, Species, Breed


class AnimalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = serializers.AnimalSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_class = AnimalFilterSet


class EntityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = serializers.EntitySerializer
    permission_classes = [AllowAny]


class MedicalRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = serializers.MedicalRecordSerializer
    permission_classes = [AllowAny]


class SpeciesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Species.objects.all()
    serializer_class = serializers.SpeciesSerializer
    permission_classes = [AllowAny]


class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = serializers.BreedSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'species_field')
