# Generated by Django 4.1.4 on 2022-12-26 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_weeklytask_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='weeklytask',
            name='color',
            field=models.CharField(default='#fad3fd', max_length=16),
        ),
    ]
