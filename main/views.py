import json
from datetime import datetime, date

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import WeeklyTask

odaylookup = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}

def index(request):
    if True:
        index = date.today().weekday()
        return render(request, 'main/index.html',{
            'preferredMode': 'Week Mode',
            'current': odaylookup[index],
            'index': index
        })

def selectcontentweek(request):
    if request.method == 'GET':
        data = request.GET.dict()
        today = date.today().day
        context = date.today()
        max = 6-today
        min = today-0
        daytask = WeeklyTask.objects.filter(date_time__day=context.day, date_time__month=context.month, date_time__year=context.year)
        print(daytask)
    return JsonResponse({}, status=200)