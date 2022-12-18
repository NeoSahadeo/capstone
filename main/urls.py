from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    
    ### Util Patterns
    path('selectcontentweek', views.selectcontentweek, name='select_content_week')
]