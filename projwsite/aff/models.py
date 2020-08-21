from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	name = models.CharField(max_length=100, blank=False, default='subscriber')
	post = models.CharField(max_length=500)
	user = models.ForeignKey(User, on_delete=models.CASCADE) 
	email = models.CharField(max_length=500, blank=False)
