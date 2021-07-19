from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model: Coordinate = Coordinate
        fields: list = ['id', 'latitude', 'longitude', 'route']


class RouteSerializer(serializers.ModelSerializer):
    coordinates: QuerySet = CoordinateSerializer(source='coordinate_set', many=True)

    class Meta:
        model: Route = Route
        fields: list = ['id', 'name', 'level', 'average_rating', 'created_at', 'creator', 'coordinates']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model: Rating = Rating
        fields: list = ['id', 'rating', 'author', 'route']
        read_only_fields: list = ['author', 'route']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model: Comment = Comment
        fields: list = ['id', 'title', 'comment', 'author', 'route']
        read_only_fields: list = ['author', 'route']