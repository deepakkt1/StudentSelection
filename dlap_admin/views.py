from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.shortcuts import render_to_response
from submit.models import Project
from student.models import Student
from django.http import HttpResponseRedirect

# Create your views here.

@csrf_exempt
def projects_mgmt(request):
	projects = Project.objects.all()
	return render(request, 'dlap_admin/projects_mgmt.html', {'projects': projects})

@csrf_exempt
def project_mgmt(request, project_id):
	project = Project.objects.get(pk=project_id)
	first_choice = Student.objects.all().filter(project1=project_id, assigned=False)
	second_choice = Student.objects.all().filter(project2=project_id, assigned=False)
	third_choice = Student.objects.all().filter(project3=project_id, assigned=False)
	fourth_choice = Student.objects.all().filter(project4=project_id, assigned=False)
	fifth_choice = Student.objects.all().filter(project5=project_id, assigned=False)
	return render(request, 'dlap_admin/project_mgmt.html', 
		{
		'project': project, 
		'first_choice': first_choice,
		'second_choice': second_choice,
		'third_choice': third_choice,
		'fourth_choice': fourth_choice,
		'fifth_choice': fifth_choice,
		})

@csrf_exempt
def update_project(request, project_id):
	
	student_id = request.POST.get('student_id','')
	
	if(student_id != "NONE"):
		student = Student.objects.filter(pk=student_id)
		student.update(assigned=True)
		student = Student.objects.get(pk=student_id)

		project = Project.objects.filter(pk=project_id)
		project.update(assigned=True)
		project.update(assigned_student=student)

	else:
		projects = Project.objects.filter(pk=project_id)
		project = Project.objects.get(pk=project_id)

		project.assigned_student.assigned = False
		project.assigned_student.save()

		projects.update(assigned=False)
		projects.update(assigned_student=None)


	return HttpResponseRedirect("/mgmt/projects/")

@csrf_exempt
def students_mgmt(request):
	students = Student.objects.all()	
	return render(request, 'dlap_admin/students_mgmt.html', {'students': students})	
