from django import forms
from django.forms import ModelForm
from django_unicorn.components import UnicornView
from ..models import WeeklyTask, User

class AddTaskForm(ModelForm):
    class Meta:
        model = WeeklyTask
        fields = ['taskname','date_time','color']

class AddtaskView(UnicornView):
    form = str(AddTaskForm())
    display = True
    