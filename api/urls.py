from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'animals', views.AnimalViewSet)
router.register(r'entities', views.EntityViewSet)
router.register(r'medical', views.MedicalRecordViewSet)


urlpatterns = [
        url(r'^', include(router.urls)),
    ]
