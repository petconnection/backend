from django.contrib.auth import views as auth_views
from django.urls import path
from backoffice import views
from django.conf import settings
from django.conf.urls.static import static


login_kwargs = {
    'template_name': 'login.html',
    'redirect_authenticated_user': True
}

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(**login_kwargs), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.home, name='home'),
    path('add', views.animal, name='add'),
    path('update/<int:animal_id>/', views.animal, name='update'),
    path('delete/<int:animal_id>/', views.delete, name='delete'),
    path('entity/', views.entity, name='entity'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
