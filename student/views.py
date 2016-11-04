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
	prev_app_radio = request.POST.get('prev_app_radio', "N/A");
	fall_employment_textarea = request.POST.get('fall_employment_textarea', "N/A");
	background_chk_radio = request.POST.get('background_chk_radio',"N/A");
	resume =  request.FILES.get('resume');
	coverletter = request.FILES.get('coverletter');
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
		background_chk_radio = background_chk_radio
	)
	student.save()
	#template = loader.get_template('submit/home.html')
        #return HttpResponse(template.render(request))
	return HttpResponseRedirect("https://dlap-web-app.herokuapp.com/")
