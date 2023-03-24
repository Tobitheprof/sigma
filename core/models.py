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
	what_will_you_use_paradox_for = models.TextField()

	def __str__(self):
		return self.owner.username

class MedicalInfo(models.Model):
	owner = models.ForeignKey(User, on_delete=models.SET_NULL)
	 

# Create your models here.
