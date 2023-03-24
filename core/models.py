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
	how_did_you_hear_about_us = models.TextField()
	what_will_you_use_sigma_for = models.TextField()
	allergies = models.TextField()
	blood_group = models.CharField(max_length=300)
	genotype = models.CharField(max_length=300)
	medical_condition = models.CharField(max_length=300)

	def __str__(self):
		return self.owner.username
	
class Chat(models.Model):
    initiator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=500000000)
    gpt = models.TextField(max_length=1700000000000000000000)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
class Doctor(models.Model):
	name = models.CharField(max_length=300)
	email = models.EmailField(unique=True)
	picture = models.ImageField(upload_to="Images")
	hospital = models.CharField(max_length=300)
	bio = models.TextField(max_length=500)
	

	def __str__(self):
		return self.name



# Create your models here.
