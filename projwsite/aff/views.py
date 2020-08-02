
from django.http import HttpResponse,request, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect

from .forms import ContactForm 	

# Create your views here.
def land(request):
	return render(request, 'landing.html')
	
def home(request):
	return render(request, 'home.html', {})

def emailView(self, request):
	template_name = 'home.html'

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.isValid():

			text = form.cleaned_data['email']
			form.save()
	args = {'form':form, 'text':text}		

	# form = ContactForm() #initializing another blank form
	return render(request, self.template_name, {'form':form}, args)
	
	# return redirect('success!')


def about(request):
	return render(request, 'about.html')

def blog(request):
	return render(request, 'blog.html')

def covers(request):
	return render(request, 'covers.html')
