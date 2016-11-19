from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^projects/update/(?P<project_id>[0-9]+)$', views.update_project, name='update_project'),
    url(r'^projects/(?P<project_id>[0-9]+)$', views.project_mgmt, name='project_mgmt'),
    url(r'^projects/', views.projects_mgmt, name='projects_mgmt'),
    url(r'^students/', views.students_mgmt, name='students_mgmt'),
    #url(r'^student/', views.student_mgmt, name='student_mgmt'),
]

