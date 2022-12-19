from datetime import date, timedelta
from django_unicorn.components import UnicornView
from ..models import WeeklyTask

today = date.today()
dayIndex = today.weekday()

class ShowtasksweeklyView(UnicornView):
    daytasks = ''
    value = dayIndex

    def dayupdate(self):
        # 'weight' describes the 'displacement'/vector from the current day to
        # the day requested by the user.
        weight = today - timedelta(days=int(dayIndex)-int(self.value))
        daytasks = WeeklyTask.objects.filter(user_id=self.request.user.id,date_time__day=weight.day, date_time__month=weight.month, date_time__year=weight.year).order_by('-date_time').values()

        self.value = self.value
        self.daytasks = daytasks


