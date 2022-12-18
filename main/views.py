import json
from datetime import datetime, date, timedelta

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

today = date.today()
dayIndex = today.weekday()

def index(request):
    if True:
        daytasks = WeeklyTask.objects.filter(user_id=request.user.id,date_time__day=today.day, date_time__month=today.month, date_time__year=today.year).order_by('-date_time')
        return render(request, 'main/index.html',{
            'preferredMode': 'Week Mode',
            'current': odaylookup[dayIndex],
            'index': dayIndex,
            'daytasks': daytasks
        })

def selectcontentweek(request):
    if request.method == 'GET':
        data = request.GET.dict()
        # 'weight' describes the 'displacement'/vector from the current day to
        # the day requested by the user. 
        weight = today - timedelta(days=int(dayIndex)-int(data['val']))
        
        daytasks = WeeklyTask.objects.filter(user_id=request.user.id,date_time__day=weight.day, date_time__month=weight.month, date_time__year=weight.year).order_by('-date_time').values()
        
        return JsonResponse({
            'daytasks': list(daytasks),
            'current': odaylookup[int(data['val'])]
        }, status=200)
    return JsonResponse({}, status=500)