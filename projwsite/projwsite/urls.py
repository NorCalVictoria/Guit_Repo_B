from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, reverse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aff.urls'))
]
