# Generated by Django 4.1.4 on 2022-12-22 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_weeklytask_color_alter_weeklytask_taskname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklytask',
            name='color',
            field=models.CharField(default='#aaf638', max_length=16),
        ),
    ]
