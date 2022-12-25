from datetime import date, timedelta
from django_unicorn.components import UnicornView
from ..models import WeeklyTask

today = date.today()
dayIndex = today.weekday()

odaylookup = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}

class ShowtasksweeklyView(UnicornView):
    showform = False
    current = odaylookup[dayIndex]
    value = dayIndex
    daytasks = None
    showtasks = True
    showtasks_polling = True

    def dayupdate(self):
        # 'weight' describes the 'displacement'/vector from the current day to
        # the day requested by the user.
        weight = today - timedelta(days=int(dayIndex)-int(self.value))
        daytasks = WeeklyTask.objects.filter(user_id=self.request.user.id, date_time__day=weight.day, date_time__month=weight.month, date_time__year=weight.year).order_by('-date_time').values()

        self.value = self.value
        self.daytasks = daytasks
        self.current = odaylookup[int(self.value)]

    def mount(self):
        ShowtasksweeklyView.dayupdate(self)

    def updated(self, name, value):
        if name == 'showform':
            ShowtasksweeklyView.dayupdate(self)
        if name == 'showform' and value == True:
            self.call("initializePlugins", 'Week Mode')