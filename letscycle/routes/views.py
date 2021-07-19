from django.db.utils import IntegrityError
from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from routes.serializers import RouteSerializer, CoordinateSerializer, RatingSerializer, CommentSerializer
from routes.models import Route, Coordinate, Rating, Comment

class AuthoredListCreateAPIView(generics.ListCreateAPIView):
    def create(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if request.user.is_anonymous:
                return Response({"errors": "User is not authorized"}, status=status.HTTP_401_UNAUTHORIZED)
            try:
                serializer.save(author=request.user, route_id=self.kwargs['route_id'])
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            except IntegrityError as error:
                return Response({"errors": str(error)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RouteChildListCreateAPIView(generics.ListCreateAPIView):
    def get_queryset(self):
        route = get_object_or_404(Route, pk=self.kwargs['route_id'])
        return self.queryset.filter(route=route)


class RouteList(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # Saving routes with the default FORMDATA
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        res = self.create_routes_by_polylines(request.data.get('polyline'), request.user)
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


class RatingList(AuthoredListCreateAPIView, RouteChildListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer



class CommentList(AuthoredListCreateAPIView, RouteChildListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
