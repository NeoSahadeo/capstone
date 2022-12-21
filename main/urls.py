from django.urls import path, re_path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('createtask', views.createtask, name='createtask'),
]