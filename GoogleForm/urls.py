from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<form_id>[0-9]+)/$', views.formDetail, name='formDetail'),
    url(r'^createForm/$', views.createForm, name='createForm'),
    url(r'^saveForm/$', views.saveForm, name='saveForm'),
    url(r'^updateForm/(?P<form_id>[0-9]+)/$', views.updateForm, name='updateForm')
]