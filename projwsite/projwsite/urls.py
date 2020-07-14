from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from aff import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('aff/', include('aff.urls')),

	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('blog/', views.blog, name='blog'),
	path('covers/', views.covers, name='covers'),
]
