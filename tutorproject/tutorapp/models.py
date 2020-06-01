from django.db import models

# Create your models he

class Post(models.Model):
    category = models.CharField(max_length=25)
    clas = models.CharField(max_length=25)
    subject = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    place_detail = models.CharField(max_length=100)
    gender = models.CharField(max_length=25)
    no_student = models.IntegerField()
    salary = models.IntegerField()
    title = models.CharField(max_length=100)
    phone = models.IntegerField()