from rest_framework import viewsets
from api.models import Animal
from api.serializers import *


class AnimalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class EntityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class MedicalRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
