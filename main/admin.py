from django.contrib import admin
from .models import User, WeeklyTask

# class UserAdmin(admin.ModelAdmin):
#     pass

# class WeeklyTasksAdmin(admin.ModelAdmin):
#     pass

admin.site.register(User)
admin.site.register(WeeklyTask)
# admin.site.register()