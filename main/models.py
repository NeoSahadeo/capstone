import random
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser, models.Model):
    preferredMode = models.CharField(default='Week Mode', max_length=100)

class WeeklyTask(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    taskname = models.CharField(max_length=200, blank=True)
    date_time = models.DateTimeField(default=None)
    color = models.CharField(max_length=16, default='FFFFFF')

    def __str__(self):
        return self.taskname

class UserImage(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
