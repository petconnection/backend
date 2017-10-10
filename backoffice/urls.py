from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views


login_args = {'template_name': 'backoffice/login.html'}

urlpatterns = [
    url(r'^login/$', auth_views.login, login_args,  name='backoffice_login'),
    url(r'^logout/$', auth_views.logout, name='backoffice_logout'),
    url(r'^home/$', views.home, name='backoffice_home'),
]


