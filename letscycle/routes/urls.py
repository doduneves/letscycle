from django.urls import path

from routes.views import *

urlpatterns = [
    path('routes/', RouteList.as_view(), name='route-list'),
    path('routes/<int:pk>/', RouteDetail.as_view(), name='route-detail'),

    path('coordinates/', CoordinateList.as_view(), name='coordinate-list'),
    path('coordinates/<int:pk>/', CoordinateDetail.as_view(), name='coordinate-detail'),
]
