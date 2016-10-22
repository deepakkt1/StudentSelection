from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^project.html$', views.project, name='project'),
    url(r'^$', views.submit, name='submit'),
]

