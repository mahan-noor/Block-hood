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
    police_contact = PhoneNumberField()
    health_contact = PhoneNumberField()

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


    def save_bs(self):
        self.save()

    def delete_bs(self):
        self.delete()

    @classmethod
    def get_all_bs(cls):
        businesses = cls.objects.all()
        return businesses
class Business(models.Model):
    bs_name = models.CharField(max_length=30)
    about = HTMLField()
    bs_user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    bs_location = models.ForeignKey(Neighborhood, related_name="businesses", on_delete=models.CASCADE)
    bs_email = models.EmailField()
    bs_pic = CloudinaryField('1920x1080')

    def save_bs(self):
        self.save()

    def delete_bs(self):
        self.delete()

    @classmethod
    def get_all_bs(cls):
        businesses = cls.objects.all()
        return businesses

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = HTMLField(max_length=70)
    post_user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    post_location = models.ForeignKey(Neighborhood, related_name="posts", on_delete=models.CASCADE)
    post_pic = CloudinaryField('1920x1080')

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_all_posts(cls):
        posts = cls.objects.all()
        return posts

