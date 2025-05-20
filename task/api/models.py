from django.db import models
from django.conf import settings


class Location(models.Model):
    street_number = models.IntegerField()
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street_number} {self.street_name}, {self.city}"


class User(models.Model):
    gender = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    picture_thumbnail = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} {self.surname} ({self.id})"
