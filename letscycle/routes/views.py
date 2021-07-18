from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.forms.models import model_to_dict

from routes.serializers import RouteSerializer, CoordinateSerializer, RatingSerializer
from routes.models import Route, Coordinate, Rating

# Create your views here.
class RouteList(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # Saving routes with the default FORMDATA
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        res = self.create_routes_by_polylines(request.data.get('polyline'),request.user)
        return Response(res, status=status.HTTP_201_CREATED)


    def create_routes_by_polylines(self, data, user=None):
        response_array = []
        for routes in data:
            r = Route()
            r.create_route_by_polylines(routes, user)
            model_to_dict(r, fields=[field.name for field in r._meta.fields])

            response_array.append(model_to_dict(r, fields=[field.name for field in r._meta.fields]))

        return response_array


class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class CoordinateList(generics.ListCreateAPIView):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer


class CoordinateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer


class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.filter(route_id=self.kwargs['pk'])
