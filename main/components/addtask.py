from datetime import date, timedelta
from django_unicorn.components import UnicornView
from ..models import WeeklyTask
from .showtasksweekly import referredValue
from django.shortcuts import render

class AddtaskView(UnicornView):
    referredValue = referredValue