from django.db import models
# Create your models here.

class Courses(models.Model):
	Course = models.CharField(max_length=255)
	Subject = models.CharField(max_length=255)
	Rating = models.DecimalField(max_digits=2, decimal_places=1)
	
	def __str__(self):
		return self.Course