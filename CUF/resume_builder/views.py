from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from .forms import UploadFileForm, ContactForm
from django.utils import timezone
from resume_builder.models import ResumeWithFileField
from handler import file_handler

def upload_file(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			data = ResumeWithFileField(name = request.POST['name'], upload_date=timezone.now(), resume_file=request.FILES['file'])
			data.save()
			data_id = data.id
			return render(request, 'resume_builder/uploaded_file.html', {
				'data':file_handler(data.id)
			})
	else:
		form = UploadFileForm()
	return render(request, 'resume_builder/upload.html', {
		'form':form,
	})

def contact(request):
	if request.method == 'POST':
		form = ContactForm()
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = ContactForm()
	return render(request, 'resume_builder/contact.html',{
		'form': form,
	})
