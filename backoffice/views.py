from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import api.models as models
from .forms import AnimalForm
from django.core.files.storage import FileSystemStorage


@login_required(login_url='login')
def delete(request, animal_id):
    models.Animal.objects.get(pk=animal_id).delete()
    return redirect(home)


@login_required(login_url='login')
def animal(request, animal_id=None):
    context = {'species': models.Species.objects.all()}
    if animal_id:
        context['animal_id'] = animal_id
        context['animal'] = models.Animal.objects.get(pk=animal_id)
        context['edit'] = True

    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():

            weight = request.POST.get('weight')

            r_breed = request.POST.get('breed')
            species = models.Species.objects.get(pk=request.POST['species'])
            if r_breed:
                breed = models.Breed.objects.get_or_create(name=r_breed, species_field=species)[0]
            else:
                breed = models.Breed.objects.get(name='Unknown', species_field=species)

            animal_pic, filename = request.FILES.get('file'), request.POST.get('pic')
            if animal_pic:
                fs = FileSystemStorage()
                filename = fs.save(animal_pic.name, animal_pic)

            animal, _ = models.Animal.objects.update_or_create(
                id = context.get('animal_id'),
                defaults = {
                    'name': request.POST.get('name'),
                    'entity': models.Entity.objects.get(user=request.user),
                    'weight': weight if weight else None,
                    'size': form.cleaned_data['size'],
                    'sex': form.cleaned_data['sex'],
                    'bio': form.cleaned_data['bio'],
                    'breed_field': breed,
                    'pic': filename
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
