from datetime import date
from django_unicorn.components import UnicornView
from ..models import WeeklyTask

today = date.today()
monthIndex = today.month

omonthlookup = {
    0: 'January',
    1: 'Febuary',
    2: 'March',
    3: 'April',
    4: 'May',
    5: 'June',
    6: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
odaylookup = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}

def generateDays(value):
    arr = []
    for x in range(1, value+1):
        arr.append(x)
    return arr

class ShowtasksmonthlyView(UnicornView):
    showform = False
    current = omonthlookup[monthIndex]
    value = monthIndex
    showtasks = True
    daytasks = None
    currentDay = None
    amountOfDays = 0
    def monthupdate(self):
        # daytasks = WeeklyTask.objects.filter(user_id=self.request.user.id, date_time__day=self.day, date_time__month=today.month, date_time__year=today.year).order_by('-date_time').values()
        # self.daytasks = daytasks
        amountOfDays = generateDays(31)
        self.value = self.value
        self.current = omonthlookup[int(self.value)]
        self.currentDay = f'{self.current} - '
        self.amountOfDays = amountOfDays
    def mount(self):
        ShowtasksmonthlyView.monthupdate(self)
        self.call('setCurrentDay', today.day)