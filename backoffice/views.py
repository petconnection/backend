from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import api.models as models
from .forms import AnimalForm


@login_required(login_url='login')
def animal(request):
    context = {
        'add': True,
        'species': models.Species.objects.all()
    }
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            r_breed = request.POST.get('breed')
            species = models.Species.objects.get(pk=request.POST['species'])
            if r_breed:
                breed = models.Breed.objects.get_or_create(name=r_breed, species_field=species)[0]
            else:
                breed = models.Breed.objects.get(name='Unknown', species_field=species)

            animal = models.Animal(
                name = request.POST.get('name'),
                entity = models.Entity.objects.get(user=request.user),
                weight = request.POST.get('weight'),
                size = form.cleaned_data['size'],
                sex = form.cleaned_data['sex'],
                bio = form.cleaned_data['bio'],
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

            return redirect(home)

        else:
            context['errors'] = form.errors.as_text()
            return render(request, 'forms/animal.html', context)

    # if it is not a POST, return template with add value for different menú
    return render(request, 'forms/animal.html', context)


@login_required(login_url='login')
def home(request):
    context = {}
    user_entity = models.Entity.objects.get(user=request.user)
    context['animals'] = models.Animal.objects.filter(entity=user_entity)
    context['species'] = models.Species.objects.all()

    return render(request, 'home.html', context)
