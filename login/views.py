#views.py
from login.forms import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from submit.models import Project
from student.models import Student

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'],
	    first_name = form.cleaned_data['first_name'],
	    )
	    return render_to_response('registration/success.html')
            #return HttpResponseRedirect('client/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
@login_required
def clientinfo(request):
    projects = Project.objects.all()
    students=Student.objects.all()
    data = list()
    p2=list()
    names=list()
    names.append("Project Name/Student Name")
    for student in students:
	names.append(student.primary_first_name)
    for i in range(0,len(projects)):
	p1=list()
	#numbers.append(str(i))
	p2.append("Project"+str(projects[i].id))
	p1.append(projects[i].app_title)
       	for student in students:
		if(student.project1 == str(projects[i].id)):		
			p1.append(1)
		elif(student.project2 == str(projects[i].id)):		
			p1.append(2)
		elif(student.project3 == str(projects[i].id)):		
			p1.append(3)
		elif(student.project4 == str(projects[i].id)):		
			p1.append(4)
		elif(student.project5 == str(projects[i].id)):		
			p1.append(5)
		else:		
			p1.append(0)
        #data.append(student) 
    	data.append(p1)
    return render_to_response(
    'registration/matrix.html',{'students':data,'projects':p2,'names':names,'student':students}
    )
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
@login_required 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    projects = Project.objects.all()
    students=Student.objects.all()
    data = list()
    p2=list()
    names=list()
    names.append("Project Name/Student Name")
    for student in students:
	names.append(student.primary_first_name)
    for i in range(0,len(projects)):
	p1=list()
	#numbers.append(str(i))
	p2.append("Project"+str(projects[i].id))
	p1.append(projects[i].app_title)
       	for student in students:
		if(student.project1 == str(projects[i].id)):		
			p1.append(1)
		elif(student.project2 == str(projects[i].id)):		
			p1.append(2)
		elif(student.project3 == str(projects[i].id)):		
			p1.append(3)
		elif(student.project4 == str(projects[i].id)):		
			p1.append(4)
		elif(student.project5 == str(projects[i].id)):		
			p1.append(5)
		else:		
			p1.append(0)
        #data.append(student) 
    	data.append(p1)
    return render_to_response(
    'registration/matrix.html',{'students':data,'projects':p2,'names':names,'student':students}
    )

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


	return HttpResponseRedirect("/client/projects/")

"""@login_required
def home(request):
    return render_to_response(
    'registration/matrix.html',
    { 'user': request.user }
    )"""
