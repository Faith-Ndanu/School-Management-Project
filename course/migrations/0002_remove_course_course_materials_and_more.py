# Generated by Django 5.0.6 on 2024-07-12 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_materials',
        ),
        migrations.RemoveField(
            model_name='course',
            name='learning_objective',
        ),
        migrations.RemoveField(
            model_name='course',
            name='teaching_method',
        ),
        migrations.AddField(
            model_name='course',
            name='number_of_students',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='number_of_units',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='scheduled_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 12, 14, 30)),
        ),
    ]
