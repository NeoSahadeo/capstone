# Generated by Django 4.1.2 on 2022-12-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_weeklytask_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklytask',
            name='color',
            field=models.CharField(default='#c02a99', max_length=16),
        ),
    ]