from django.urls import path
from .views import TravelAPI, HotelAPI, KlassAPI

urlpatterns = [
    path('api/v1/travels/', TravelAPI.as_view()),
    path('api/v1/travel/<int:pk>/', TravelAPI.as_view()),

    path('api/v1/hotels/', HotelAPI.as_view()),
    path('api/v1/hotel/<int:pk>/', HotelAPI.as_view()),

    path('api/v1/klasses/', KlassAPI.as_view()),
    path('api/v1/klass/<int:pk>/', KlassAPI.as_view())
]