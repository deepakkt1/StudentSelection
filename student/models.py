from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
	primary_first_name = models.CharField(max_length=255)
	primary_last_name = models.CharField(max_length=255)
	optradio = models.CharField(max_length=255)
	ethnic_type = models.CharField(max_length=255)
	bldr_addr = models.CharField(max_length=1024)
	bldr_phone_number = models.CharField(max_length=255)
	bldr_email = models.EmailField()
	student_number = models.CharField(max_length=255)
	student_department = models.CharField(max_length=255)
	gpa = models.CharField(max_length=12)
	school_level_select = models.CharField(max_length=255)
	grad_date_select = models.CharField(max_length=255)
	year_select = models.CharField(max_length=255)
	last_digits_ssn = models.CharField(max_length=255)
	resume = models.FileField(upload_to='resumes')
	coverletter = models.FileField(upload_to='coverletters')
	summer_addr = models.CharField(max_length=255)
	summer_phone_number = models.CharField(max_length=255)
	summer_email = models.EmailField()
	secondary_major = models.CharField(max_length=255)
	optradio_research = models.CharField(max_length=255)
	prev_app_radio = models.CharField(max_length=255)
	fall_employment_textarea = models.CharField(max_length=1024)
	background_chk_radio = models.CharField(max_length=255)
