from django.http import HttpResponse
from django.shortcuts import render
from .models import WeeklyTask

def index(request):
    if True:
        return render(request, 'main/index.html',{
            'preferredMode': 'Week Mode',
    })

def createtask(request):
    # if request.method == "GET":
        # value = request.method["POST"]
        # newtask = WeeklyTask(user_id=request.user.id, date_time)
    # else:
    pass
