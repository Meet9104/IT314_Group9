from django.db import models

from django.contrib.auth.models import AbstractUser

from djongo import models
# Create your models here.


class User(AbstractUser):
    is_faculty= models.BooleanField('Is faculty', default=False)
    is_ta = models.BooleanField('Is ta', default=False)
    is_student = models.BooleanField('Is student', default=False)




class ExampleModel(models.Model):
    title = models.CharField(max_length=100,default='a')
    description = models.TextField(default='error')
    objects = models.DjongoManager()
 