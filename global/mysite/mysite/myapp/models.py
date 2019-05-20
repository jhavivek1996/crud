from django.db import models

class start(models.Model):
	name=models.CharField(max_length=255)
	roll=models.CharField(max_length=255)
	date=models.DateField()
	
