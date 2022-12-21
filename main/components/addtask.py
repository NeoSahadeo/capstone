from django import forms
from django_unicorn.components import UnicornView
from ..models import WeeklyTask, User

class AddTaskForm(forms.Form):
    title = forms.CharField(required=True)

class AddtaskView(UnicornView):
    form_class = AddTaskForm
    title = ''
    display = False

    # Resets form fields
    def updated(self, name, value):
        self.title = ''
