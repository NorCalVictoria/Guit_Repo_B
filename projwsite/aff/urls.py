from django.urls import path, reverse
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('landing/', views.land, name='land'),
	path('home/', views.home,name='home'),
	path('about/', views.about, name='about'),
	path('blog/', views.blog, name='blog'),
	path('covers/', views.covers, name='covers'),
	path('post/',views.home, name='email'),
]
