import datetime
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
from .models import User, WeeklyTask
from .forms import RegisterForm, LoginForm

def index(request):
    if True:
        return render(request, 'main/index.html',{
            'preferredMode': 'Week Mode',
    })

def profile(request):
    if request.user.is_authenticated:
        id = request.user.id
        user = User.objects.get(id = id)
        return render(request, 'main/profile.html',{
            'userinfo': user,
        })
    else:
        return render(request, 'main/login.html',{
            'form': LoginForm(),
            'message': 'Login is required to view your profile.'
        })

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirm_password"]
        if password != confirmation:
            return render(request, "main/register.html", {
                "message": "Passwords must match.",
                'form': RegisterForm()
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()

        except IntegrityError:
            return render(request, "main/register.html", {
                "message": "Username already taken.",
                'form': RegisterForm()
            })
        login_auth(request, user)
        return HttpResponseRedirect(reverse("main:index"))
    else:
        return render(request, "main/register.html", {
            'form': RegisterForm()
        })

def login(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login_auth(request, user)
            return HttpResponseRedirect(reverse("main:index"))
        else:
            return render(request, "main/login.html", {
                "message": "Invalid username and/or password.",
                'form': LoginForm()
            })
    else:
        return render(request, "main/login.html", {
            'form': LoginForm()
        })

def logout(request):
    logout_auth(request)
    return HttpResponseRedirect(reverse("main:index"))

def createtask(request):
    if request.method == 'POST':
        taskname = request.POST['body[taskname]']
        color = request.POST['body[color]']
        date_time = datetime.datetime.strptime(request.POST['body[date_time]'], '%Y %m %d %H %M')
        newtask = WeeklyTask(
            user_id = User.objects.get(id=request.user.id),
            taskname = taskname,
            date_time = date_time,
            color = color
        )
        newtask.save()
    return HttpResponse('')