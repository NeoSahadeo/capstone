from datetime import date
from calendar import monthrange
from django_unicorn.components import UnicornView
from ..models import WeeklyTask

today = date.today()
monthIndex = today.month-1

omonthlookup = {
    0: 'January',
    1: 'Febuary',
    2: 'March',
    3: 'April',
    4: 'May',
    5: 'June',
    6: 'July',
    7: 'August',
    8: 'September',
    9: 'October',
    10: 'November',
    11: 'December'
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
    # monthrange return tuple, I want the second value
    value = monthrange(today.year, value)[1]
    arr = []
    for x in range(1, value+1):
        arr.append(x)
    return arr

def formatdate(date_time):
    return f'{str(date_time).split()[0]} {str(date_time).split()[1][0:5]}'
    
class ShowtasksmonthlyView(UnicornView):
    showform = False
    showtask = False
    showtasks = True
    current = omonthlookup[monthIndex]
    value = monthIndex
    init_value = None
    fetchtask = None
    daytasks = None
    currentDay = None
    icurrentDay = None
    task_id = None
    amountOfDays = 0

    def monthupdate(self, day):
        amountOfDays = int(self.value)+1
        self.value = self.value
        self.current = omonthlookup[int(self.value)]
        self.currentDay = f'{self.current} - {day}'
        self.icurrentDay = day
        self.amountOfDays = generateDays(amountOfDays)
        if today.month != int(self.value)+1:
            self.call('setCurrentDay', day)
            ShowtasksmonthlyView.setSimilar(self, value=day)
        else:
            ShowtasksmonthlyView.setSimilar(self, value=today.day)

    def mount(self):
        ShowtasksmonthlyView.monthupdate(self, today.day)
        self.call('setCurrentDay', today.day)
        daytasks = WeeklyTask.objects.filter(user_id=self.request.user.id, date_time__day=today.day, date_time__month=today.month, date_time__year=today.year).order_by('-date_time').values()
        self.daytasks = daytasks
        self.init_value = self.value

    def updated(self, name, value):
        print(name,value)
        if int(value) == monthIndex and name == 'value':
            ShowtasksmonthlyView.setSimilar(self, value=today.day)
            ShowtasksmonthlyView.monthupdate(self, today.day)
            self.call('setCurrentDay', today.day)
            return None
        if name == 'showtasks' and value == True:
            return None
        if name == 'icurrentDay':
            self.call('setCurrentDay', int(value))
            ShowtasksmonthlyView.setSimilar(self, value=value)
            return None
        if name == 'showform' and value == True:
            self.call("initializePlugins", 'Month Mode')
            return None
        if name == 'showform' and value == False:
            self.call('refresh')
            return None
        if name == 'showtask' and value == False:
            self.call('refresh')
            return None
        if name == 'task_id':
            fetchtask = WeeklyTask.objects.get(user_id=self.request.user.id, id=int(value))
            self.fetchtask = fetchtask
            self.call('formatdate_time', formatdate(fetchtask.date_time))
            self.call("initializePlugins", 'Month Mode')
            return None
        self.call('setCurrentDay', 1)
        ShowtasksmonthlyView.monthupdate(self,1)        

    def setSimilar(self, **kwargs):
        value = kwargs['value']
        daytasks = WeeklyTask.objects.filter(user_id=self.request.user.id, date_time__day=int(value), date_time__month=int(self.value)+1, date_time__year=today.year).order_by('-date_time').values()
        self.daytasks = daytasks
        self.currentDay = f'{self.current} - {value}'
        self.icurrentDay = int(value)