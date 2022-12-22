import random
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class WeeklyTask(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    taskname = models.CharField(max_length=200, blank=True)
    date_time = models.DateTimeField(default=None)
    color = models.CharField(max_length=16, default="#%06x" % random.randint(0, 0xFFFFFF))

    def __str__(self):
        return self.taskname
    