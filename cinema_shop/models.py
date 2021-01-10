from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Projection(models.Model):
    movie_name = models.CharField(max_length=45)
    movie_time = models.TimeField(null=False)
    hall_capacity = models.IntegerField(null=False)
    users = models.ManyToManyField(User, through='Card')

    def get_absolute_url(self):
        return f"/projections/{self.id}/"

    def __str__(self):
        return self.movie_name


class Card(models.Model):
    movie = models.ForeignKey(Projection, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_number = models.IntegerField(null=False)

