from django.db import models

class Users(models.Model):
	name = models.CharField(max_length = 30)
	psw = models.CharField(max_length = 32)
	score = models.IntegerField(blank=True, null=True)
	update_time = models.DateField(blank=True, null=True)

class Hackmes(models.Model):
	score = models.IntegerField()
	title = models.TextField()
	problem = models.TextField()
	tip = models.TextField()
	true = models.BooleanField()
	result = models.TextField()