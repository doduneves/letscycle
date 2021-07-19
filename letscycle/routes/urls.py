from django.urls import path

from routes.views import *

urlpatterns = [
    path('routes/', RouteList.as_view(), name='route-list'),
    path('routes/<int:pk>/', RouteDetail.as_view(), name='route-detail'),

    path('coordinates/', CoordinateList.as_view(), name='coordinate-list'),
    path('coordinates/<int:pk>/', CoordinateDetail.as_view(), name='coordinate-detail'),

    path('routes/<int:route_id>/ratings/', RatingList.as_view(), name='rating-list'),

    path('routes/<int:route_id>/comments/', CommentList.as_view(), name='comment-list'),
    path('routes/<int:route_id>/comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),


]
