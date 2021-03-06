from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from aff import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('/', include('aff.urls')),   # Is this correct  the /   ???

	path('', views.land, name='land'),
	path('landing/', views.land, name='land'),
	path('home/',views.home,name='home'),
	path('about/', views.about, name='about'),
	path('blog/', views.blog, name='blog'),
	path('covers/', views.covers, name='covers'),
] +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
