from django.contrib.auth import views as auth_views
from django.conf.urls import url
from backoffice import views


urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'},  name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^$', views.home, name='home'),
]

