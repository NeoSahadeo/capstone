# Generated by Django 4.1.4 on 2022-12-25 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_user_image_alter_weeklytask_color_delete_uploadimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='weeklytask',
            name='color',
            field=models.CharField(default='#4eae16', max_length=16),
        ),
    ]
