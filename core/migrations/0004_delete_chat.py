# Generated by Django 4.0 on 2023-03-25 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_course_doctor_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chat',
        ),
    ]