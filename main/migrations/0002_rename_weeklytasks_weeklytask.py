# Generated by Django 4.1.2 on 2022-12-18 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WeeklyTasks',
            new_name='WeeklyTask',
        ),
    ]