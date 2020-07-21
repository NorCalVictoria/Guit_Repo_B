from django.shortcuts import render
from django.http import HttpResponse,request

# Create your views here.
def land(request):
	return render(request, 'landing.html')
def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html')

def blog(request):
	return render(request, 'blog.html')

def covers(request):
	return render(request, 'covers.html')