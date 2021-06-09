# Generated by Django 3.2.4 on 2021-06-09 11:14

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('hood', '0001_initial'),
    ]

    operations = [
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
    ]
