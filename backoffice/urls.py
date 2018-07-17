from django.contrib.auth import views as auth_views
from django.conf.urls import url
from backoffice import views
from django.conf import settings
from django.conf.urls.static import static


login_kwargs = {
    'template_name': 'login.html',
    'redirect_authenticated_user': True
}

urlpatterns = [
    url(r'^login/$', auth_views.login, login_kwargs,  name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^$', views.home, name='home'),
    url(r'^add$', views.animal, name='add'),
    url('^update/(?P<animal_id>[\w-]+)$', views.animal, name='update'),
    url('^delete/(?P<animal_id>[\w-]+)$', views.delete, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
