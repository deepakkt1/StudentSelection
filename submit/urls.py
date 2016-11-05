from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^project_form.html$', views.project_form, name='project_form'),
    url(r'^project_list/$', views.project_list, name='project_list'),
    url(r'^search/facultydept/$', views.searchfacultydept, name='search_faculty_dept'),
    url(r'^search/studentmajor/$', views.searchstudentmajor, name='search_student_major'),
    url(r'^search/projectname/$', views.searchprojectname, name='search_project_name'),
    url(r'^search/facultyname/$', views.searchfacultyname, name='search_faculty_name'),
    url(r'^search/$', views.searchall, name='search_all_projects'),
    url(r'^(?P<project_id>[0-9]+)$', views.project, name='project'),
    url(r'^$', views.submit, name='submit'),
]

