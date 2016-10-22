from __future__ import unicode_literals

from django.db import models

# Create your models here.

CATEGORIES = (
    ('AER','Aerospace Engineering Sciences '),
    ('APM','Applied Math' ),
    ('CBE','Chemical & Biological Engineering'),
    ('CEA','Civil, Environmental & Architectural Engineering '),
    ('CSE','Computer Science'),
    ('ECE','Electrical, Computer & Energy Engineering'),
    ('Phy','Physics'),
    ('EEn','Environmental Engineering'),
    ('MEn','Mechanical Engineering'),
    ('CSG','Colorado Space Grant'),
    ('EnE','Engineering Education' ),
    ('ATL','ATLAS'),
)

CHOICES=[('Yes','Yes'),('No','No')]

class Project(models.Model):
	primary_first_name = models.CharField(max_length=255)
	primary_last_name = models.CharField(max_length=255)
	primary_phone_number = models.CharField(max_length=255) 
	primary_email = models.EmailField()
	primary_faculty_dept = models.CharField(max_length=12)
	primary_eng_focus= models.CharField(max_length=3)
	
	secondary_first_name = models.CharField(max_length=255)
	secondary_last_name = models.CharField(max_length=255)
	secondary_phone_number = models.CharField(max_length=255) 
	secondary_email = models.EmailField()
	secondary_faculty_dept = models.CharField(max_length=12)

	grad_first_name = models.CharField(max_length=255)
	grad_last_name = models.CharField(max_length=255)
	grad_phone_number = models.CharField(max_length=255) 
	grad_email = models.EmailField()

	app_title = models.CharField(max_length=255)
	app_url = models.CharField(max_length=255)
	special_reqs = models.CharField(max_length=255)
	full_desc = models.CharField(max_length=1024)
	recruit_fields = models.CharField(max_length=512)

	supervision_status = models.CharField(max_length=255)
	supervision_contact = models.CharField(max_length=255)
	work_nature = models.CharField(max_length=255)
	prior_work = models.CharField(max_length=255)
	desired_student = models.CharField(max_length=255)
	speed_type = models.CharField(max_length=255)
	account_contact = models.CharField(max_length=255)
	eng_dev_communities = models.CharField(max_length=255)
