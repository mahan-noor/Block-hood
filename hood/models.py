from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=30)
    neighborhood_location = models.CharField(max_length=30)
    neighborhood_pic = CloudinaryField("1920x1080")
    occupants_count = models.IntegerField(null=True)

    @classmethod
    def get_all_neighborhoods(cls):
        neighborhoods = cls.objects.all()
        return neighborhoods


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    neighborhood = models.ManyToManyField(Neighborhood)
    email = models.EmailField()
    profile_pic = CloudinaryField('1080x1080')
    bio = HTMLField()
