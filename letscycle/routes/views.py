from django.shortcuts import render
from rest_framework import generics

from routes.serializers import RouteSerializer
from routes.models import Route

# Create your views here.
class RouteList(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
