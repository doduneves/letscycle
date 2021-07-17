from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class Route(models.Model):
    class Level(models.IntegerChoices):
        BEGINNER = 1, _('Beginner')
        REGULAR = 2, _('Regular')
        PROFESSIONAL = 3, _('Professional')

    name = models.CharField(max_length=255)
    level = models.IntegerField(choices=Level.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    # @property
    # def average_rating(self):
    #     return self.rating_set.all()


class Location(models.Model):
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    routes = models.ManyToManyField(Route)


class Coordinate(models.Model):
    latitute = models.FloatField()
    longitude = models.FloatField()

    route = models.ForeignKey(Route, on_delete=models.CASCADE)


class Rating(models.Model):
    class Meta:
        unique_together = ('author', 'route')

    level = models.CharField(max_length=255)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)


class Comment(models.Model):
    title = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
