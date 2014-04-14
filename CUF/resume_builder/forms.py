from django import forms
from resume_builder.models import ResumeWithFileField

class UploadFileForm(forms.Form):
	name = forms.CharField(max_length=255)
	file = forms.FileField()

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
