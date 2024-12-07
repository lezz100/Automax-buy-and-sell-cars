import json
import os
from django.db import models
from django.contrib.auth.models import User
from .utils import user_directory_path

def load_kenya_counties():

    filepath = os.path.join(os.path.dirname(__file__), 'Counties.json')
    with open(filepath, 'r') as file:
        return json.load(file)

KENYA_COUNTIES = [(county, county) for county in load_kenya_counties()]

class Location(models.Model):
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    county = models.CharField(max_length=128, choices=KENYA_COUNTIES)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.county}, {self.city}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path, null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'


