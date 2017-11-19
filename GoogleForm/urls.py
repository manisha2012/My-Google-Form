from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<form_id>[0-9]+)/$', views.formDetail, name='formDetail'),
    url(r'^createForm/$', views.createForm, name='createForm'),
    url(r'^saveForm/$', views.saveForm, name='saveForm'),
    url(r'^updateForm/(?P<form_id>[0-9]+)/$', views.updateForm, name='updateForm')
]
