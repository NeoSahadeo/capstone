# Generated by Django 4.1.4 on 2022-12-20 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_weeklytask_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklytask',
            name='color',
            field=models.CharField(default='#63d07d', max_length=16),
        ),
    ]
