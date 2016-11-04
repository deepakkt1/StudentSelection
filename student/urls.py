from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.studinfo, name='studentsubmit'),
    url(r'^student.html$', views.student, name='student'),
]

