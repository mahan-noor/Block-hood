from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=30)
    neighborhood_location = models.CharField(max_length=30)
    neighborhood_pic = ImageField(blank=True, manual_crop="1920x1080")
    occupants_count = models.IntegerField(null=True)