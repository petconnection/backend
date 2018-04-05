from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import api.models as models
from .forms import AnimalForm


@login_required(login_url='login')
def animal(request, animal_id=None):
    context = {'species': models.Species.objects.all()}
    if animal_id:
        context['animal_id'] = animal_id
        context['animal'] = models.Animal.objects.get(pk=animal_id)

    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            r_breed = request.POST.get('breed')
            species = models.Species.objects.get(pk=request.POST['species'])
            if r_breed:
                breed = models.Breed.objects.get_or_create(name=r_breed, species_field=species)[0]
            else:
                breed = models.Breed.objects.get(name='Unknown', species_field=species)

            animal, created = models.Animal.objects.update_or_create(
                id = context.get('animal_id'),
                defaults = {
                    'name': request.POST.get('name'),
                    'entity': models.Entity.objects.get(user=request.user),
                    'weight': request.POST.get('weight'),
                    'size': form.cleaned_data['size'],
                    'sex': form.cleaned_data['sex'],
                    'bio': form.cleaned_data['bio'],
                    'breed_field': breed
                }
            )

            models.MedicalRecord.objects.update_or_create(
                animal = animal,
                defaults = {
                    'vaccines': request.POST.get('vaccines'),
                    'castrated': request.POST.get('is-castrated') is not None,
                    'chip': request.POST.get('has-chip') is not None,
                    'comments': request.POST.get('comments')
                }
            )

            return redirect(home)

        else:
            context['errors'] = True
            return render(request, 'forms/animal.html', context)

    return render(request, 'forms/animal.html', context)


@login_required(login_url='login')
def home(request):
    context = {}
    user_entity = models.Entity.objects.get(user=request.user)
    context['animals'] = models.Animal.objects.filter(entity=user_entity)
    context['species'] = models.Species.objects.all()
    context['home'] = True

    return render(request, 'home.html', context)
