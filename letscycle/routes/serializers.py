from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ['id', 'latitude', 'longitude', 'route']


class RouteSerializer(serializers.ModelSerializer):
    coordinates = CoordinateSerializer(source='coordinate_set', many=True)

    class Meta:
        model = Route
        fields = ['id', 'name', 'level', 'average_rating', 'created_at', 'creator', 'coordinates']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'rating', 'author', 'route']