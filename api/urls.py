from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('animals', views.AnimalViewSet)
router.register('entities', views.EntityViewSet)
router.register('species', views.SpeciesViewSet)
router.register('breeds', views.BreedViewSet)


urlpatterns = [
        path('', include(router.urls)),
    ]
