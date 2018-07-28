from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'animals', views.AnimalViewSet)
router.register(r'entities', views.EntityViewSet)
router.register(r'species', views.SpeciesViewSet)
router.register(r'breeds', views.BreedViewSet)


urlpatterns = [
        url(r'^', include(router.urls)),
    ]
