from django.contrib.auth import views as auth_views
from django.conf.urls import url
from backoffice import views


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
]
