import os
from django.http import HttpResponse
from wsgiref.util import FileWrapper
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
import logging
from django.db.models import Max
import collections
import csv


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

@login_required
@csrf_exempt
def download_matrix(request):
	list1=["Project Title","Faculty First Name","Faculty Last Name","Faculty Department","Assignment Status","Assigned Student First Name","Assigned Student Last Name"]
	projects=Project.objects.all()
	with open('assignedmatrix.xls','wb') as myfile:
		wr=csv.writer(myfile, quoting=csv.QUOTE_ALL)
		wr.writerow(list1)
		for pro in projects:
			li=[]
			li.append(pro.app_title)
			li.append(pro.primary_first_name)
			li.append(pro.primary_last_name)
			li.append(pro.primary_faculty_dept)
			li.append(pro.assigned)
			if(pro.assigned == False):
				li.append("")
				li.append("")
			else:
				li.append(pro.assigned_student.primary_first_name)
				li.append(pro.assigned_student.primary_last_name)
			wr.writerow(li)	
	filename = "assignedmatrix.xls" # Select your file here.                                
	wrapper = FileWrapper(file(filename))
	response = HttpResponse(wrapper, content_type='text/plain')
	response['Content-Length'] = os.path.getsize(filename)
        response['Content-Disposition'] = 'attachment; filename=assignedmatrix.xls'
	return response
	#return render(request, 'dlap_admin/projects_mgmt.html', {'projects': projects})
@login_required
@csrf_exempt
def projects_assign(request):
	projects = Project.objects.all()
	students = Student.objects.all()
	removep=[]
	numberofst={}
	for project in projects:
		hasStudents="False"
		counts=0
		for student in students:
			if not student.project1 == "N/A":
				if int(student.project1) == int(project.id):
					hasStudents="True"	
					counts+=1					
			if not student.project2 == "N/A":
				if int(student.project2) == int(project.id):
					hasStudents="True"
					counts+=1					
			if not student.project3 == "N/A":
				if int(student.project3) == int(project.id):
					hasStudents="True"
					counts+=1					
			if not student.project4 == "N/A":
				if int(student.project4) == int(project.id):
					hasStudents="True"					
					counts+=1
			if not student.project5 == "N/A":
				if int(student.project5) == int(project.id):
					hasStudents="True"					
					counts+=1
		if(hasStudents == "False"):
			removep.append(project.app_title)
		else:
			numberofst[project.id]=counts
	for ite in removep:
		projects=projects.exclude(app_title=ite)
	#assignment to projects that have few applicants, we consider the 3 least projects
	e=collections.Counter(numberofst)
	least_common=sorted(e.iteritems(), key=lambda x: x[::-1])
	for i in range(0,4):
		project_id=least_common[i][0]
		project = projects.filter(pk=project_id)
		first_choice = Student.objects.all().filter(project1=project_id, assigned=False, gpa__gte =3,project1requirements=True,prev_work="No",full_year_avail="True")
		second_choice = Student.objects.all().filter(project2=project_id, assigned=False, gpa__gte =3,project2requirements=True,prev_work="No",full_year_avail="True")
		third_choice = Student.objects.all().filter(project3=project_id, assigned=False, gpa__gte =3,project3requirements=True,prev_work="No",full_year_avail="True")
		dictofstuds={}
		if(len(first_choice)>0 and len(second_choice)>0 and len(third_choice)>0):
			first_choicegpa=first_choice.annotate(Max('gpa'))
			second_choicegpa=second_choice.annotate(Max('gpa'))
			third_choicegpa=third_choice.annotate(Max('gpa'))
			for fs in first_choicegpa:
				dictofstuds[fs.id]=fs.gpa
			for fs in second_choicegpa:
				dictofstuds[fs.id]=fs.gpa
			for fs in third_choicegpa:
				dictofstuds[fs.id]=fs.gpa
			d_s=OrderedDict()
			for w in sorted(dictofstuds, key=dictofstuds.get, reverse=True):
				d_s[w]=dictofstuds[w]
			new_dict = []
			for pair in d_s.items():
			    if d_s.values()[0] == pair[1]:
			    	new_dict.append(pair[0])
			finalstudents=[]
			for st in new_dict:
				finalstudents.append(Student.objects.get(pk=st))
			lc=0
			sid=0
			for f in finalstudents:
				if(f.cfactor>=lc):
					lc=f.cfactor	
					sid=f.id
			student = Student.objects.filter(pk=sid)
			student.update(assigned=True)
			student = Student.objects.get(pk=sid)

			project = Project.objects.filter(pk=project_id)
			project.update(assigned=True)
			project.update(assigned_student=student)
			continue
		elif(len(first_choice)>0):
			first_choicegpa=first_choice.annotate(Max('gpa'))
			lc=0
			sid=0
			for f in first_choicegpa:
				if(f.cfactor>lc):
					lc=f.cfactor	
					sid=f.id
			student = Student.objects.filter(pk=sid)
			student.update(assigned=True)
			student = Student.objects.get(pk=sid)

			project = Project.objects.filter(pk=project_id)
			project.update(assigned=True)
			project.update(assigned_student=student)
			continue
		elif(len(second_choice)>0):
			second_choicegpa=second_choice.annotate(Max('gpa'))
			lc=0
			sid=0
			for f in second_choicegpa:
				if(f.cfactor>lc):
					lc=f.cfactor	
					sid=f.id
			student = Student.objects.filter(pk=sid)
			student.update(assigned=True)
			student = Student.objects.get(pk=sid)

			project = Project.objects.filter(pk=project_id)
			project.update(assigned=True)
			project.update(assigned_student=student)
			continue
		elif(len(third_choice)>0):
			third_choicegpa=third_choice.annotate(Max('gpa'))
			lc=0
			sid=0
			for f in third_choicegpa:
				if(f.cfactor>lc):
					lc=f.cfactor	
					sid=f.id
			student = Student.objects.filter(pk=sid)
			student.update(assigned=True)
			student = Student.objects.get(pk=sid)

			project = Project.objects.filter(pk=project_id)
			project.update(assigned=True)
			project.update(assigned_student=student)
			continue
	for i in range(4,len(least_common)):
		project_id=least_common[i][0]
		project = projects.filter(pk=project_id)
		first_choice = Student.objects.all().filter(project1=project_id, assigned=False, gpa__gte =3,project1requirements=True,prev_work="No",full_year_avail="True")
		second_choice = Student.objects.all().filter(project2=project_id, assigned=False, gpa__gte =3,project2requirements=True,prev_work="No",full_year_avail="True")
		third_choice = Student.objects.all().filter(project3=project_id, assigned=False, gpa__gte =3,project3requirements=True,prev_work="No",full_year_avail="True")
		fourth_choice = Student.objects.all().filter(project4=project_id, assigned=False, gpa__gte =3,project4requirements=True,prev_work="No",full_year_avail="True")
		fifth_choice = Student.objects.all().filter(project5=project_id, assigned=False, gpa__gte =3,project5requirements=True,prev_work="No",full_year_avail="True")
		dictofstuds={}
		if(len(first_choice)>0 and len(second_choice)>0 and len(third_choice)>0 and len(fourth_choice)>0 and len(fifth_choice)>0 ):
			first_choicegpa=first_choice.annotate(Max('gpa'))
			second_choicegpa=second_choice.annotate(Max('gpa'))
			third_choicegpa=third_choice.annotate(Max('gpa'))
			fourth_choicegpa=fourth_choice.annotate(Max('gpa'))
			fifth_choicegpa=fifth_choice.annotate(Max('gpa'))
			for fs in first_choicegpa:
				dictofstuds[fs.id]=fs.gpa
			for fs in second_choicegpa:
				dictofstuds[fs.id]=fs.gpa
			for fs in third_choicegpa:
				dictofstuds[fs.id]=fs.gpa
			for fs in fourth_choicegpa:
				dictofstuds[fs.id]=fs.gpa
			for fs in fifth_choicegpa:
				dictofstuds[fs.id]=fs.gpa
			d_s=OrderedDict()
			for w in sorted(dictofstuds, key=dictofstuds.get, reverse=True):
				d_s[w]=dictofstuds[w]
			new_dict = []
			for pair in d_s.items():
			    if d_s.values()[0] == pair[1]:
			    	new_dict.append(pair[0])
			finalstudents=[]
			for st in new_dict:
				finalstudents.append(Student.objects.get(pk=st))
			lc=0
			sid=0
			for f in finalstudents:
				if(f.cfactor>=lc):
					lc=f.cfactor	
					sid=f.id
			student = Student.objects.filter(pk=sid)
			student.update(assigned=True)
			student = Student.objects.get(pk=sid)

			project = Project.objects.filter(pk=project_id)
			project.update(assigned=True)
			project.update(assigned_student=student)
			continue
		elif(len(first_choice)>0):
			first_choicegpa=first_choice.annotate(Max('gpa'))
			lc=0
			sid=0
			for f in first_choicegpa:
				if(f.cfactor>lc):
					lc=f.cfactor	
					sid=f.id
			student = Student.objects.filter(pk=sid)
			student.update(assigned=True)
			student = Student.objects.get(pk=sid)

			project = Project.objects.filter(pk=project_id)
			project.update(assigned=True)
			project.update(assigned_student=student)

			continue
		elif(len(second_choice)>0):
			second_choicegpa=second_choice.annotate(Max('gpa'))
			lc=0
			sid=0
			for f in second_choicegpa:
				if(f.cfactor>lc):
					lc=f.cfactor	
					sid=f.id
			student = Student.objects.filter(pk=sid)
			student.update(assigned=True)
			student = Student.objects.get(pk=sid)

			project = Project.objects.filter(pk=project_id)
			project.update(assigned=True)
			project.update(assigned_student=student)
			continue
		elif(len(third_choice)>0):
			third_choicegpa=third_choice.annotate(Max('gpa'))
			lc=0
			sid=0
			for f in third_choicegpa:
				if(f.cfactor>lc):
					lc=f.cfactor	
					sid=f.id
			student = Student.objects.filter(pk=sid)
			student.update(assigned=True)
			student = Student.objects.get(pk=sid)

			project = Project.objects.filter(pk=project_id)
			project.update(assigned=True)
			project.update(assigned_student=student)
		elif(len(fourth_choice)>0):
			fourth_choicegpa=fourth_choice.annotate(Max('gpa'))
			lc=0
			sid=0
			for f in fourth_choicegpa:
				if(f.cfactor>lc):
					lc=f.cfactor	
					sid=f.id
			student = Student.objects.filter(pk=sid)
			student.update(assigned=True)
			student = Student.objects.get(pk=sid)

			project = Project.objects.filter(pk=project_id)
			project.update(assigned=True)
			project.update(assigned_student=student)
		elif(len(fifth_choice)>0):
			fifth_choicegpa=fifth_choice.annotate(Max('gpa'))
			lc=0
			sid=0
			for f in fifth_choicegpa:
				if(f.cfactor>lc):
					lc=f.cfactor	
					sid=f.id
			student = Student.objects.filter(pk=sid)
			student.update(assigned=True)
			student = Student.objects.get(pk=sid)

			project = Project.objects.filter(pk=project_id)
			project.update(assigned=True)
			project.update(assigned_student=student)
	return render(request, 'dlap_admin/suc.html',)
#	return render(request, 'dlap_admin/projects_mgmt.html', {'projects': projects})



@login_required
@csrf_exempt
def projects_mgmt(request):
	projects = Project.objects.all()
	students = Student.objects.all()
	removep=[]
	for project in projects:
		hasStudents="False"
		for student in students:
			if not student.project1 == "N/A":
				if int(student.project1) == int(project.id):
					hasStudents="True"					
			if not student.project2 == "N/A":
				if int(student.project2) == int(project.id):
					hasStudents="True"					
			if not student.project3 == "N/A":
				if int(student.project3) == int(project.id):
					hasStudents="True"					
			if not student.project4 == "N/A":
				if int(student.project4) == int(project.id):
					hasStudents="True"					
			if not student.project5 == "N/A":
				if int(student.project5) == int(project.id):
					hasStudents="True"					
		if(hasStudents == "False"):
			removep.append(project.app_title)
	for ite in removep:
		projects=projects.exclude(app_title=ite)
	return render(request, 'dlap_admin/projects_mgmt.html', {'projects': projects})

@login_required
@csrf_exempt
def project_mgmt(request, project_id):
	project = Project.objects.get(pk=project_id)
	first_choice = Student.objects.all().filter(project1=project_id, assigned=False, gpa__gte =3,project1requirements=True)
	second_choice = Student.objects.all().filter(project2=project_id, assigned=False, gpa__gte =3,project2requirements=True)
	third_choice = Student.objects.all().filter(project3=project_id, assigned=False, gpa__gte =3,project3requirements=True)
	fourth_choice = Student.objects.all().filter(project4=project_id, assigned=False, gpa__gte =3,project4requirements=True)
	fifth_choice = Student.objects.all().filter(project5=project_id, assigned=False, gpa__gte =3,project5requirements=True)
	return render(request, 'dlap_admin/project_mgmt.html', 
		{
		'project': project, 
		'first_choice': first_choice,
		'second_choice': second_choice,
		'third_choice': third_choice,
		'fourth_choice': fourth_choice,
		'fifth_choice': fifth_choice,
		})
@login_required
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
