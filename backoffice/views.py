from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import api.models as models
from .forms import AnimalForm
from django.utils import timezone
from django.http import JsonResponse as json


@login_required(login_url='login')
def home(request):
    from django.contrib.auth import authenticate
    context = {}
    user_entity = models.Entity.objects.get(user=request.user)
    context['animals'] = models.Animal.objects.filter(entity=user_entity)
    context['species'] = models.Species.objects.all()
    
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            r_breed = request.POST.get('breed')
            print(request.POST)
            species = models.Species.objects.get(pk=request.POST['species'])
            if r_breed:
                breed = models.Breed.objects.get_or_create(name=r_breed, species_field=species)[0]
            else: 
                breed = models.Breed.objects.get(name='Unknown', species_field=species)
            
            animal = models.Animal(
                name = request.POST.get('name'),
                entity = user_entity,
                weight = request.POST.get('weight'),
                size = form.cleaned_data['size'],
                sex = form.cleaned_data['sex'],
                bio = form.cleaned_data['bio'],
                registration = timezone.now(),
                breed_field = breed
            )
            
            animal.save()
            
            md_record = models.MedicalRecord(
                animal = animal,
                vaccines = request.POST.get('vaccines'),
                castrated = request.POST.get('is-castrated') is not None,
                chip = request.POST.get('has-chip') is not None,
                comments = request.POST.get('comments')
            )
            
            md_record.save()
            return json({'message': 'Animal successfully created'}, status=200)
            
        else:
            return json({'message': form.errors.as_text()}, status=500)
            
    return render(request, 'home.html', context)
