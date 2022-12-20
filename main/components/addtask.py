from django import forms
from django.core import serializers
from django_unicorn.components import UnicornView
from .showtasksweekly import referredValue

class GenerateForm(forms.Form):
    title = forms.CharField(required=True)
    
    def serialize(self):
        return {
            'title': self.title
        }  

class AddtaskView(UnicornView):
    referredValue = referredValue
    