from django.db import models

# Create your models here.

class Student(models.Model):
    st_name = models.CharField(max_length=20)
    st_id = models.IntegerField()
    st_phone_no = models.IntegerField()
    st_address = models.CharField(max_length=50)