from django.db import models

# Create your models here.
class Resume(models.Model):
	name = models.CharField(max_length=255)
	upload_date = models.DateTimeField('date published')
	file_path = models.CharField(max_length=255)
	def __unicode__(self):
		return self.name		

class ResumeWithFileField(models.Model):
	name = models.CharField(max_length=255)
	upload_date = models.DateTimeField('date published')
	resume_file = models.FileField(upload_to='resumes/')

	def __unicode__(self):
		return self.name
