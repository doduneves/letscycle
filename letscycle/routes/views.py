import json

from django.db.models.query import QuerySet
from django.db.utils import IntegrityError
from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.serializers import ModelSerializer

from routes.serializers import RouteSerializer, CoordinateSerializer, RatingSerializer, CommentSerializer
from routes.models import Route, Coordinate, Rating, Comment


class AuthoredListCreateAPIView(generics.ListCreateAPIView):
    def create(self, request, **kwargs: dict):
        serializer: ModelSerializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if request.user.is_anonymous:
                return Response({"errors": "User is not authorized"}, status=status.HTTP_401_UNAUTHORIZED)
            try:
                serializer.save(author=request.user, route_id=self.kwargs['route_id'])
                headers: dict = self.get_success_headers(serializer.data)
                return Response({serializer.data}, status=status.HTTP_201_CREATED, headers=headers)
            except IntegrityError as error:
                return Response({"errors": str(error)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RouteChildListCreateAPIView(generics.ListCreateAPIView):
    def get_queryset(self):
        route: Route = get_object_or_404(Route, pk=self.kwargs['route_id'])
        return self.queryset.filter(route=route)


class RouteList(generics.ListCreateAPIView):
    queryset: QuerySet = Route.objects.all()
    serializer_class: ModelSerializer = RouteSerializer
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]


    def list(self, request):
        serializer: ModelSerializer = RouteSerializer(self.get_queryset(), many=True)
        if request.accepted_renderer.format == 'html':
            return Response({'routes': serializer.data }, template_name='routes/list.html')

        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        serializer: ModelSerializer = self.get_serializer(data=request.data)

        # Saving routes with the default FORMDATA
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        res = self.create_routes_by_polylines(request.data.get('polyline'), request.user)
        return Response(res, status=status.HTTP_201_CREATED)


    def create_routes_by_polylines(self, data, user=None):
        response_array: list = []
        for routes in data:
            r: Route = Route()
            r.create_route_by_polylines(routes, user)
            model_to_dict(r, fields=[field.name for field in r._meta.fields])

            response_array.append(model_to_dict(r, fields=[field.name for field in r._meta.fields]))

        return response_array


class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset: QuerySet = Route.objects.all()
    serializer_class: ModelSerializer = RouteSerializer
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'routes/read.html'

    def retrieve(self, request, *args, **kwargs):
        route = self.get_object()
        serializer = self.get_serializer(route)
        if request.accepted_renderer.format == 'html':
            return Response({'route': serializer.data }, template_name='routes/read.html')

        return Response(serializer.data)



class CoordinateList(generics.ListCreateAPIView):
    queryset: QuerySet = Coordinate.objects.all()
    serializer_class: ModelSerializer = CoordinateSerializer


class CoordinateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset: QuerySet = Coordinate.objects.all()
    serializer_class: ModelSerializer = CoordinateSerializer


class RatingList(AuthoredListCreateAPIView, RouteChildListCreateAPIView):
    queryset: QuerySet = Rating.objects.all()
    serializer_class: ModelSerializer = RatingSerializer


class CommentList(AuthoredListCreateAPIView, RouteChildListCreateAPIView):
    queryset: QuerySet = Comment.objects.all()
    serializer_class: ModelSerializer = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset: QuerySet = Comment.objects.all()
    serializer_class: ModelSerializer = CommentSerializer
