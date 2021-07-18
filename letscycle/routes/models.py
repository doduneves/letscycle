from django.db import models, transaction
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


    def create_route_by_polylines(self, coordinates, user):
        self.name = f'New Created Route - {user}'
        self.level = 1 if len(coordinates) < 200 else 2 if len(coordinates) < 1000 else 3
        self.creator = user
        self.save()
        self.create_coordinates(coordinates)


    @transaction.atomic
    def create_coordinates(self, route_data):
        self.coordinate_set.all().delete()
        for item in route_data:
            self.coordinate_set.create(
                latitude = item[0],
                longitude = item[1],
            )



class Location(models.Model):
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    routes = models.ManyToManyField(Route)


class Coordinate(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    route = models.ForeignKey(Route, on_delete=models.CASCADE)


class Rating(models.Model):
    class Meta:
        unique_together = ('author', 'route')

    rating = models.CharField(max_length=255)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)


class Comment(models.Model):
    title = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
