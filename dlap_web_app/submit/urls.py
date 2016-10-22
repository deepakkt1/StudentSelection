from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^project_form.html$', views.project_form, name='project_form'),
    url(r'^project_list.html$', views.project_list.as_view(), name='project_list'),
    url(r'^(?P<project_id>[0-9]+)$', views.project, name='project'),
    url(r'^$', views.submit, name='submit'),
]

