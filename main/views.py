import datetime
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse, redirect
from .models import User, WeeklyTask, UserImage
from .forms import RegisterForm, LoginForm
from .threads import run_continuously

def threads():
    # Start the background thread
    try:
        stop_run_continuously.set()
    except:
        stop_run_continuously = run_continuously()

def index(request):
    if request.user.is_authenticated == True:
        threads()
        return render(request, 'main/index.html',{
            'username': User.objects.get(id=request.user.id).username,
            'preferredMode': User.objects.get(id=request.user.id).preferredMode,
            'profileimage': UserImage.objects.get(user_id=request.user.id).image
        })
    return redirect("main:login")

def profile(request):
    if request.user.is_authenticated:
        threads()
        id = request.user.id
        user = User.objects.get(id = id)
        profileimage = UserImage.objects.get(user_id=user.id).image.url
        return render(request, 'main/profile.html',{
            'userinfo': user,
            'profileimage': profileimage,
            'form': RegisterForm(),
        })
    else:
        return render(request, 'main/login.html',{
            'form': LoginForm(),
            'message': 'Login is required to view your profile.',
        })

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        image = request.POST['image']
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirm_password"]
        if password != confirmation:
            return render(request, "main/register.html", {
                "message": "Passwords must match.",
                'form': RegisterForm()
            })

        # Attempt to create new user
        results = User.objects.filter(username=username)
        if len(results) == 0:
            user = User.objects.create_user(username,email,password)
            user.save()
            user = User.objects.get(username=username)
            if image != '':
                uploadedimage = UserImage(user_id=user,image=image)
                uploadedimage.save()
            else:
                uploadedimage = UserImage(user_id=user)
                uploadedimage.save()
            login_auth(request, user)
            return HttpResponseRedirect(reverse("main:index"))            
        else:
            return render(request, "main/register.html", {
                "message": "Username already taken.",
                'form': RegisterForm()
            })
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
    return HttpResponseRedirect(reverse("main:login"))

def createtask(request):
    if request.method == 'POST':
        taskname = request.POST['body[taskname]']
        color = request.POST['body[color]']
        id = int(request.POST['body[task_id_number]'])
        allow_delete = request.POST['body[allow_delete]']
        date_time = datetime.datetime.strptime(request.POST['body[date_time]'], '%Y %m %d %H %M')
        if allow_delete == 'true':
            task = WeeklyTask.objects.get(id=int(id))
            task.delete()
            return HttpResponse()
        # -1 describes that a new task must be created
        # as it does not exist within the context
        if id == -1:
            task = WeeklyTask(
                user_id = User.objects.get(id=request.user.id),
                taskname = taskname,
                date_time = date_time,
                color = color
            )
            task.save()
        else:
            task = WeeklyTask.objects.get(id=id)
            task.taskname = taskname
            task.color = color
            task.date_time = date_time
            task.save(update_fields=['taskname','color','date_time'])
    return HttpResponse('')

def switchmode(request):
    if request.method == 'GET' and request.user.is_authenticated == True:
        user = User.objects.get(id=request.user.id)
        user.preferredMode = request.GET['body[mode]']
        user.save(update_fields=['preferredMode'])
    return HttpResponse()

def updateprofile(request):
    if request.method == 'POST':
        try:
            image = request.FILES['image']
            try:
                image = request.FILES['image']
                uploadedimage = UserImage.objects.get(user_id=request.user.id)
                uploadedimage.delete()
                uploadedimage = UserImage(user_id=User.objects.get(id=request.user.id), image=image)
                uploadedimage.save()
            except:
                uploadedimage = UserImage(user_id=User.objects.get(id=request.user.id), image=image)
                uploadedimage.save()
        except:
            try:
                username = request.POST['username']
                user = User.objects.get(id=request.user.id)
                user.username = username
                user.save(update_fields=['username'])
            except IntegrityError:
                id = request.user.id
                user = User.objects.get(id = id)
                profileimage = UserImage.objects.get(user_id=user.id).image.url
                return render(request, 'main/profile.html',{
                    'userinfo': user,
                    'profileimage': profileimage,
                    'form': RegisterForm(),
                    "message": "Username already taken.",
                })
    return redirect('main:profile')