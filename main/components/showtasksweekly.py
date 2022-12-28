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

def formatdate(date_time):
    return f'{str(date_time).split()[0]} {str(date_time).split()[1][0:5]}'

class ShowtasksweeklyView(UnicornView):
    showform = False
    showtask = False
    showtasks = True
    current = odaylookup[dayIndex]
    value = dayIndex
    daytasks = None
    init_value = None
    fetchtask = None
    task_id = None
    showtasks_polling = True
    weight = None

    def dayupdate(self,day):
        # 'weight' describes the 'displacement'/vector from the current day to
        # the day requested by the user.
        weight = today - timedelta(days=int(dayIndex)-int(self.value))
        daytasks = WeeklyTask.objects.filter(user_id=self.request.user.id, date_time__day=weight.day, date_time__month=weight.month, date_time__year=weight.year).order_by('-date_time').values()
        self.value = day
        self.daytasks = daytasks
        self.current = odaylookup[int(self.value)]
        self.weight = weight

    def mount(self):
        self.init_value = dayIndex
        ShowtasksweeklyView.dayupdate(self , dayIndex)

    def updated(self, name, value):
        if name == 'showform' and value == True:
            self.call("initializePlugins", 'Week Mode')
        if name == 'showtasks' and value == True:
            self.init_value = self.value
            ShowtasksweeklyView.dayupdate(self, self.value)
            self.call('refresh')
        if name == 'task_id':
            fetchtask = WeeklyTask.objects.get(user_id=self.request.user.id, id=int(value))
            self.fetchtask = fetchtask
            self.call('formatdate_time', formatdate(fetchtask.date_time))
            self.call("initializePlugins", 'Week Mode')
        if name == 'value':
            ShowtasksweeklyView.dayupdate(self, value)
