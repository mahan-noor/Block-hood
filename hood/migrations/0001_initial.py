# Generated by Django 3.2.4 on 2021-06-09 19:00

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighborhood_name', models.CharField(max_length=30)),
                ('neighborhood_location', models.CharField(max_length=30)),
                ('neighborhood_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='1920x1080')),
                ('occupants_count', models.IntegerField(null=True)),
                ('police_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('health_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='1080x1080')),
                ('bio', tinymce.models.HTMLField()),
                ('neighborhood', models.ManyToManyField(to='hood.Neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=30)),
                ('description', tinymce.models.HTMLField(max_length=70)),
                ('post_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('post_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='1920x1080')),
                ('post_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='hood.neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('bs_name', models.CharField(max_length=30)),
                ('about', tinymce.models.HTMLField()),
                ('bs_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('bs_email', models.EmailField(max_length=254)),
                ('bs_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='1920x1080')),
                ('bs_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='hood.neighborhood')),
            ],
        ),
    ]
