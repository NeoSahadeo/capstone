from django import forms
from django_unicorn.components import UnicornView

class AddTaskForm(forms.Form):
    title = forms.CharField(required=True)

class AddtaskView(UnicornView):
    form_class = AddTaskForm
    title = ''

    def submit(self):
        print(self.title)
        self.validate()