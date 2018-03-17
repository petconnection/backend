from rest_framework import serializers
from api.models import Animal, Entity, MedicalRecord, Species, Breed


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        exclude = ['animal']


class AnimalSerializer(serializers.ModelSerializer):
    breed = serializers.SerializerMethodField('get_breed_field')
    medical_record = MedicalRecordSerializer(read_only=True)

    @staticmethod
    def get_breed_field(obj):
        return obj.breed_field.id

    class Meta:
        model = Animal
        exclude = ['breed_field']


class EntitySerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Entity
        exclude = ['user']


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):
    species = serializers.ReadOnlyField(source='species_field.id')

    class Meta:
        model = Breed
        exclude = ['species_field']
