from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('api')

admin_models = list(filter(lambda x: x[0] != 'baseclass', app.models.items()))

for model_name, model in admin_models:
    admin.site.register(model)
