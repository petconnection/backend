from django.urls import path
from register import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('<str:code>/', views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
