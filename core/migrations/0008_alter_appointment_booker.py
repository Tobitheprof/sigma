# Generated by Django 4.0 on 2023-04-02 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0007_alter_appointment_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='booker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]