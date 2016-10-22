from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.views.generic import ListView

from .models import Project

# Create your views here.

@csrf_exempt
def project_form(request):
    template = loader.get_template('submit/project_form.html')
    return HttpResponse(template.render(request))

def project(request, project_id):
	project = Project.objects.get(pk=project_id)
	return render(request, 'submit/project.html', {'project': project})

class project_list(ListView):
	model = Project    
 	template_name = 'submit/project_list.html'

@csrf_exempt
def submit(request):
	fname = request.POST.get('primary_first_name', "N/A");
	lname = request.POST.get('primary_last_name', "N/A");
	email = request.POST.get('primary_email', "N/A");
	phone = request.POST.get('primary_phone_number', "N/A");
	focus = request.POST.get('primary_eng_focus', "N/A");
	faculty_dept = request.POST.get('primary_faculty_dept', "N/A");
	secondary_first_name = request.POST.get('secondary_first_name',"N/A");
	secondary_last_name = request.POST.get('secondary_last_name',"N/A");
	secondary_email = request.POST.get('secondary_email',"N/A");
	secondary_phone_number = request.POST.get('phone_number',"N/A");
	secondary_faculty_dept = request.POST.get('secondary_faculty_dept',"N/A");
	grad_first_name = request.POST.get('grad_first_name',"N/A");
	grad_last_name = request.POST.get('grad_last_name',"N/A");
	grad_phone_number = request.POST.get('grad_phone_number',"N/A");
	grad_email = request.POST.get('grad_email',"N/A");
	app_title = request.POST.get('app_title',"N/A");
	app_url = request.POST.get('app_url',"N/A");
	special_reqs = request.POST.get('special_reqs',"N/A");
	full_desc = request.POST.get('full_desc',"N/A");
	listStudMajor = request.POST.getlist('listStudMajor',"N/A");
	supervision_status = request.POST.get('supervision_status',"N/A");
	supervision_contact = request.POST.get('supervision_contact',"N/A");
	work_nature = request.POST.get('work_nature',"N/A");
	prior_work = request.POST.get('prior_work',"N/A");
	desired_student = request.POST.get('desired_student',"N/A");
	speed_type = request.POST.get('speed_type',"N/A");
	account_contact = request.POST.get('account_contact',"N/A");
	eng_dev_communities = request.POST.get('eng_dev_communities',"N/A");

	project = Project(
		primary_first_name = fname, 
		primary_last_name = lname, 
		primary_phone_number = phone, 
		primary_eng_focus = focus, 
		primary_faculty_dept = faculty_dept, 
		primary_email = email,
		
		secondary_first_name = secondary_first_name,
		secondary_last_name = secondary_last_name,
		secondary_phone_number = secondary_phone_number,
		secondary_email = secondary_email,
		secondary_faculty_dept = secondary_faculty_dept,

		grad_first_name = grad_first_name,
		grad_last_name = grad_last_name,
		grad_phone_number = grad_phone_number,
		grad_email = grad_email,

		app_title = app_title,
		app_url = app_url,
		special_reqs = special_reqs,
		full_desc = full_desc,
		recruit_fields = listStudMajor,

		supervision_status = supervision_status,
		supervision_contact = supervision_contact,
		work_nature = work_nature,
		prior_work = prior_work,
		desired_student = desired_student,
		speed_type = speed_type,
		account_contact = account_contact,
		eng_dev_communities = eng_dev_communities
	)

	project.save()
        template = loader.get_template('submit/home.html')
        return HttpResponse(template.render(request))

