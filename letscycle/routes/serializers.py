from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Route


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'name', 'level', 'created_at', 'creator']
