import threading
import datetime
import time
import schedule
from .utilities import pushnotification
from .models import WeeklyTask

def run_continuously(interval=1):
    cease_continuous_run = threading.Event()
    
    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)
                
    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run

# A refrence I use for the datetime format
# 2022-12-29 00:00:00
prev = None
def background_job():
    now = datetime.datetime.now()
    date_time = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute)
    weeklytasks = WeeklyTask.objects.filter(date_time=date_time)
    global prev
    if prev == None:
        prev = date_time
    if prev != date_time:
        prev = date_time
        for tasks in weeklytasks:
            pushnotification(tasks)

schedule.every().second.do(background_job)