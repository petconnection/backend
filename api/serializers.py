from rest_framework import serializers
from api.models import Animal, Entity, MedicalRecord


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        exclude = ['animal']


class AnimalSerializer(serializers.ModelSerializer):
    breed_field = serializers.ReadOnlyField(source='breed_field.name')
    medical_record = MedicalRecordSerializer(read_only=True)

    class Meta:
        model = Animal
        fields = '__all__'


class EntitySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Entity
        fields = '__all__'
