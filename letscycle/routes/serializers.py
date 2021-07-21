from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model: Coordinate = Coordinate
        fields: list = ['id', 'latitude', 'longitude', 'route']


class RatingSerializer(serializers.ModelSerializer):
    rated_by = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model: Rating = Rating
        fields: list = ['id', 'rating', 'author', 'route', 'rated_by']
        read_only_fields: list = ['author', 'route']


class CommentSerializer(serializers.ModelSerializer):
    commented_by = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model: Comment = Comment
        fields: list = ['id', 'title', 'comment', 'author', 'route', 'commented_by']
        read_only_fields: list = ['author', 'route']


class RouteSerializer(serializers.ModelSerializer):
    coordinates: QuerySet = CoordinateSerializer(source='coordinate_set', many=True)
    ratings: QuerySet = RatingSerializer(source='rating_set', read_only=True, many=True)
    comments: QuerySet = CommentSerializer(source='comment_set', read_only=True, many=True)
    creator = serializers.CharField(source="creator.username", read_only=True)
    display_level = serializers.CharField(source="get_level_display", read_only=True)

    class Meta:
        model: Route = Route
        fields: list = [
            'id',
            'name',
            'display_level',
            'level',
            'average_rating',
            'created_at',
            'creator',
            'coordinates',
            'ratings',
            'comments'
        ]
