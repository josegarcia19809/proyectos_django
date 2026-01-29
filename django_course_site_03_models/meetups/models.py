from django.db import models


# Create your models here.

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    city = models.CharField(max_length=100)
    date = models.DateField()
    attendees = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
