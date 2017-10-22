from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.models import Animal, Entity


@login_required(login_url='backoffice_login')
def home(request):
    context = {}
    user_entity = Entity.objects.filter(user=request.user)[0]
    context['animals'] = Animal.objects.filter(entity=user_entity)

    return render(request, 'backoffice/home.html', context)
