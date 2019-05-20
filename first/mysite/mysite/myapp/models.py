from django.db import models

class game(models.Model):
	g_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)
	price=models.CharField(max_length=255)
	size=models.CharField(max_length=255)
	date=models.DateField(max_length=255)
	class Meta:
		db_table = "game"