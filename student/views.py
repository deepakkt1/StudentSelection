from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from submit.models import Project
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
# Create your views here.

@csrf_exempt
def student(request):
	project = Project.objects.all()
	return render_to_response('student/student.html',{'project':project})
	   
	

@csrf_exempt
def studinfo(request):
	cfactor=0
	fname = request.POST.get('primary_first_name', "N/A");
	lname = request.POST.get('primary_last_name', "N/A");
	optradio = request.POST.get('optradio',"N/A");
	ethnic_radio = request.POST.getlist('ethnic_type', "N/A");
	#full_desc = request.POST.get('full_desc',"N/A");
	bldr_addr = request.POST.get('bldr_addr',"N/A");
	bldr_phone_number = request.POST.get('bldr_phone_number',"N/A");
	bldr_email = request.POST.get('bldr_email',"N/A");
	student_number = request.POST.get('student_number',"N/A");
	student_department = request.POST.get('student_department', "N/A");
	gpa = request.POST.get('gpa', "N/A");
	school_level_select = request.POST.get('school_level_select', "NA");
	grad_date_select = request.POST.get('grad_date_select', "NA");
	year_select = request.POST.get('year_select', "NA");
	last_digits_ssn = request.POST.get('last_digits_ssn', "NA");
	summer_addr = request.POST.get('summer_addr', "NA");
	summer_phone_number = request.POST.get('summer_phone_number',"N/A");
	summer_email = request.POST.get('summer_email',"N/A");
	secondary_major = request.POST.get('secondary_major', "N/A");
	optradio_research = request.POST.get('optradio_research', "N/A");
	prev_app_radio = request.POST.get('prev_app', "N/A");
	fall_employment_textarea = request.POST.get('fall_employment_textarea', "N/A");
	background_chk_radio = request.POST.get('background_chk_radio',"N/A");
	project1requirements = request.POST.get('proj1final',"N/A");
	project2requirements = request.POST.get('proj2final',"N/A");
	project3requirements = request.POST.get('proj3final',"N/A");
	project4requirements = request.POST.get('proj4final',"N/A");
	project5requirements = request.POST.get('proj5final',"N/A");
	full_year_avail = request.POST.get('full_year_avail',"N/A");
	prev_work = request.POST.get('prev_work',"N/A");
	resume =  request.FILES.get('resume');
	coverletter = request.FILES.get('coverletter');
	project1 = request.POST.get('project1',"N/A");
	project2 = request.POST.get('project2',"N/A");
	project3 = request.POST.get('project3',"N/A");
	project4 = request.POST.get('project4',"N/A");
	project5 = request.POST.get('project5',"N/A");
	discrimination_training = request.POST.get('discrimination_training',"N/A");
	if(optradio=="Female"):
		cfactor+=1
	if('BA' in ethnic_radio or 'NHPS' in ethnic_radio or 'AN' in ethnic_radio):
		cfactor+=1
	if(prev_app_radio == "Yes"):
		cfactor+=1
	if(school_level_select =="5th year Senior"):
		cfactor+=1
	student = Student(
		primary_first_name = fname, 
		primary_last_name = lname, 
		optradio = optradio,
		ethnic_type = ethnic_radio,
		bldr_addr = bldr_addr,
		bldr_phone_number = bldr_phone_number,
		bldr_email = bldr_email,
		student_number = student_number,
		student_department = student_department,
		gpa = gpa,
		school_level_select = school_level_select,
		grad_date_select = grad_date_select,
		year_select = year_select,
		last_digits_ssn = last_digits_ssn,
		summer_addr = summer_addr,
		summer_phone_number = summer_phone_number,
		summer_email = summer_email,
		secondary_major = secondary_major,
		optradio_research = optradio_research,
		prev_app_radio = prev_app_radio,
		fall_employment_textarea = fall_employment_textarea,
		resume = resume,
		coverletter = coverletter,
		background_chk_radio = background_chk_radio,
		project1requirements = project1requirements,
		project2requirements = project2requirements,
		project3requirements = project3requirements,
		project4requirements = project4requirements,
		project5requirements = project5requirements,
		full_year_avail = full_year_avail,
		prev_work = prev_work,
		discrimination_training=discrimination_training,
		cfactor=cfactor,
		project1 = project1,
		project2 = project2,
		project3 = project3,
		project4 = project4,
		project5 = project5
	)
	student.save()
	#template = loader.get_template('submit/home.html')
        #return HttpResponse(template.render(request))
	return HttpResponseRedirect("https://dlap-web-app.herokuapp.com/")
