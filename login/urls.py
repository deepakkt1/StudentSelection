from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login',name='client'),
    #url(r'^viewmatrix$', views.clientinfo, name='view'),
    #url(r'^student.html$', views.student, name='client'),
    url(r'^logout/$', views.logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success),
    url(r'^home/$', views.home),
    url(r'^projects/update/(?P<project_id>[0-9]+)$', views.update_project, name='update_project'),
    url(r'^projects/(?P<project_id>[0-9]+)$', views.project_mgmt, name='project_mgmt'),
    url(r'^projects/', views.projects_mgmt, name='projects_mgmt'),
    url(r'^projectsassign/', views.projects_assign, name='projects_assign'),
    url(r'^downloadmatrix/', views.download_matrix, name='download_matrix'),
]

