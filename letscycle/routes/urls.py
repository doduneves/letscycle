from django.urls import path

from routes import views

urlpatterns = [
    path('routes/', views.RouteList.as_view(), name='route-list'),
    path('routes/<int:pk>/', views.RouteDetail.as_view(), name='route-detail'),
]
