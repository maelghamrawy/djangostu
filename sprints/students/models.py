from django.db import models

# Create your models here.

class students(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    age = models.IntegerField(null=True)

class course(models.Model):
    course_name = models.CharField(max_length=255)
    