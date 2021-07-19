from django.contrib.auth.models import User
from django.db import models, transaction
from django.db.models.query import QuerySet
from django.utils.translation import gettext as _

from datetime import datetime

class Route(models.Model):
    class Level(models.IntegerChoices):
        BEGINNER = 1, _('Beginner')
        REGULAR = 2, _('Regular')
        PROFESSIONAL = 3, _('Professional')

    name: str = models.CharField(max_length=255)
    level: str = models.IntegerField(choices=Level.choices)
    created_at: datetime = models.DateTimeField(auto_now_add=True)

    creator: User = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def average_rating(self) -> float:
        ratings: QuerySet = self.rating_set.all().values()
        rating_sum: int = 0

        for r in ratings:
            rating_sum += float(r['rating'])

        return rating_sum/len(ratings) if len(ratings) > 0 else None


    def create_route_by_polylines(self, coordinates: list, user: User):
        self.name = f'New Created Route - {user}'
        self.level = 1 if len(coordinates) < 200 else 2 if len(coordinates) < 1000 else 3
        self.creator = user
        self.save()
        self.create_coordinates(coordinates)


    @transaction.atomic
    def create_coordinates(self, route_data: list):
        self.coordinate_set.all().delete()
        for item in route_data:
            self.coordinate_set.create(
                latitude = item[0],
                longitude = item[1],
            )


class Location(models.Model):
    city: str = models.CharField(max_length=255)
    state: str = models.CharField(max_length=255)
    country: str = models.CharField(max_length=255)

    routes: QuerySet = models.ManyToManyField(Route)


class Coordinate(models.Model):
    latitude: float = models.FloatField()
    longitude: float = models.FloatField()

    route: Route = models.ForeignKey(Route, on_delete=models.CASCADE)


class Rating(models.Model):
    class Meta:
        unique_together = ('author', 'route')

    rating: float = models.FloatField()

    author: User = models.ForeignKey(User, on_delete=models.CASCADE)
    route: Route = models.ForeignKey(Route, on_delete=models.CASCADE)


class Comment(models.Model):
    title: str = models.CharField(max_length=255)
    comment: str = models.CharField(max_length=255)
    created_at: datetime = models.DateTimeField(auto_now_add=True)

    author: User = models.ForeignKey(User, on_delete=models.CASCADE)
    route: User = models.ForeignKey(Route, on_delete=models.CASCADE)
