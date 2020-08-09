from django.views.generic import TemplateView

from django.shortcuts import render, redirect

from .forms import ContactForm 	


# Create your views here.
def land(request):
	return render(request, 'landing.html')


def home(request):
	form = ContactForm()
	if request.method == 'POST':

		# print(request.user)
		# print(request.POST)
		form = ContactForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			form = ContactForm()
	context = {'form':form}
	return render(request, 'home.html', context)


	args = {'form': form, 'text': text}
	return render(request, self.template_name, args)
 
def about(request):
	return render(request, 'about.html')

def blog(request):
	return render(request, 'blog.html')

def covers(request):
	return render(request, 'covers.html')
