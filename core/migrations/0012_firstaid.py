# Generated by Django 4.0 on 2023-03-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_course_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstAid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('date_published', models.DateField(auto_now_add=True)),
                ('featured_image', models.ImageField(upload_to='First Aid')),
                ('body', models.TextField()),
            ],
        ),
    ]