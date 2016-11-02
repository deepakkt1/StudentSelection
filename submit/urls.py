from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^project_form.html$', views.project_form, name='project_form'),
    url(r'^project_list.html$', views.project_list.as_view(), name='project_list'),
    url(r'^project_listmajor.html$', views.project_listmajor.as_view(), name='project_listmajor'),
    url(r'^(?P<project_id>[0-9]+)$', views.project, name='project'),
    url(r'^$', views.submit, name='submit'),
    #url(r'^search/$', views.search),
    url(r'listbydept', views.projectbydept, name ='submit/listbydept/'),
    url(r'listbyfaculty', views.projectbyfaculty, name ='submit/listbyfaculty/'),
    url(r'listbymajor', views.projectbymajor, name ='submit/listbymajor/'),
    url(r'listbyprimarydept', views.projectbyfacultydept, name ='submit/listbyprimarydept/'),
    url(r'^bytitle.html$', views.showpage),
]

