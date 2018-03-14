from rest_framework import serializers
from api.models import Animal, Entity, MedicalRecord, Species, Breed


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        exclude = ['animal']


class AnimalSerializer(serializers.ModelSerializer):
    breed = serializers.SerializerMethodField('get_breed_field')
    medical_record = MedicalRecordSerializer(read_only=True)

    class Meta:
        model = Animal
        exclude = ['breed_field']

    @staticmethod
    def get_breed_field(obj):
        return obj.breed_field.id


class EntitySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Entity
        fields = '__all__'


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'
