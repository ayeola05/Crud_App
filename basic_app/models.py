from django.db import models

# Create your models here.

class School(models.Model):
	name = models.CharField(max_length=200, null=True)
	principal = models.CharField(max_length=200, null=True)
	location = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=200, null=True)
	age = models.PositiveIntegerField()
	school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='stds')

	def __str__(self):
		return self.name