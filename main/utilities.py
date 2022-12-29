from .models import User
from webpush.utils import send_to_subscription
from webpush import send_user_notification

def pushnotification(task):
    payload = {"head": "Task", "body": task.taskname}
    send_user_notification(user=User.objects.get(username=task.user_id), payload=payload, ttl=1000)