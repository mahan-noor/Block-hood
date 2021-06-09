from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField





# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=30)
    neighborhood_location = models.CharField(max_length=30)
    neighborhood_pic = CloudinaryField("1920x1080")
    occupants_count = models.IntegerField(null=True)