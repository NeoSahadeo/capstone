# Generated by Django 4.1.2 on 2022-12-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_weeklytask_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklytask',
            name='color',
            field=models.CharField(default='#965fde', max_length=16),
        ),
    ]
