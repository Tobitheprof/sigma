from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from autoslug import AutoSlugField
User = get_user_model()



class Profile(models.Model):
	owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	id_user = models.IntegerField(null=True)
	phone_number = models.IntegerField(null=True)
	how_did_you_hear_about_us = models.TextField(null=True)
	what_will_you_use_sigma_for = models.TextField(null=True)
	allergies = models.TextField(null=True)
	blood_group = models.CharField(max_length=300, null=True)
	genotype = models.CharField(max_length=300, null=True)
	medical_condition = models.CharField(max_length=300, null=True)

	def __str__(self):
		return self.owner.username
	
class Chat(models.Model):
    initiator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=500000000, null=True)
    gpt = models.TextField(max_length=1700000000000000000000, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.text
    
class Doctor(models.Model):
	name = models.CharField(max_length=300, null=True)
	email = models.EmailField(unique=True)
	phone_number = models.CharField(max_length=300, null=True)
	picture = models.ImageField(upload_to="Images")
	hospital = models.CharField(max_length=300, null=True)
	bio = models.TextField(max_length=500, null=True)

	def __str__(self):
		return self.name

class Appointment(models.Model):
    booker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
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
    description = models.TextField()

    def __str__(self):
        return self.title

class Lecture(models.Model):
    title = models.CharField(max_length=300)
    video_link = models.CharField(max_length=900,null=False)
    description = models.TextField(null=True)
    serial_number = models.IntegerField(null=True)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, null=False)

    def __str__(self):
        return self.title


# Create your models here.
