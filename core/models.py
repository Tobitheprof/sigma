from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from autoslug import AutoSlugField
User = get_user_model()

CHOICES = (
     ('yes', 'yes'),
     ('no', 'no')
)
CATEGORIES = (
     ('Self Health','Self Health'),
     ('Mental Health', 'Mental Health'),
     ('Psycology', 'Psycology'),
     ('Dental Health', 'Dental Health'),
     ('Care Giving', 'Care Giving'),
     ('Physical Fitness and Exercise', 'Physical Fitness and Exercise'),
)


class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id_user = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=300)
    how_did_you_hear_about_us = models.TextField()
    what_will_you_use_sigma_for = models.TextField()
    allergies = models.CharField(max_length=400)
    blood_group = models.CharField(max_length=300)
    genotype = models.CharField(max_length=300)
    medical_conditions = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    nationality = models.CharField(max_length=300)
    medical_history = models.TextField()
    about_me = models.TextField()

    def __str__(self):
        return self.owner.username
    
class FirstAid(models.Model):
    title = models.CharField(max_length=400)
    slug = AutoSlugField(populate_from="title", editable=False, primary_key=True)
    date_published = models.DateField(auto_now_add=True)
    featured_image = models.ImageField(upload_to="First Aid")
    body = models.TextField()

    def __str__(self):
        return self.title





class Doctor(models.Model):
    name = models.CharField(max_length=500, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=300, primary_key=True, unique=True)
    picture = models.ImageField(upload_to="Images")
    hospital = models.CharField(max_length=300, )
    bio = models.TextField(max_length=500, )
    area_of_specialization = models.CharField(max_length=300, )
    approved = models.CharField(choices=CHOICES, max_length=250)


    def __str__(self):
	    return self.name


class Appointment(models.Model):
    booker = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=300)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    last_name = models.CharField(max_length=300)
    date_booked = models.DateField(auto_now_add=True, )
    subject = models.CharField(max_length=150)
    email_address = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.booker.username

class Course(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from="title", unique=True)
    featured_image = models.ImageField(upload_to="Course Images")
    author = models.CharField(max_length=100)
    number_of_lectures = models.CharField(max_length=300)
    category = models.CharField(max_length=300, choices=CATEGORIES)
    description = models.TextField()

    def __str__(self):
        return self.title

class Lecture(models.Model):
    title = models.CharField(max_length=300)
    video_link = models.CharField(max_length=900)
    description = models.TextField()
    serial_number = models.IntegerField()
    course = models.ForeignKey(Course, on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return self.title


# Create your models here.
