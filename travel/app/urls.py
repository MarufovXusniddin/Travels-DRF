from django.urls import path
from .views import TravelAPI, TravelDetailAPI, HotelAPI, HotelDetailAPI, KlassAPI, KlassDetailAPI

urlpatterns = [
    path('api/v1/travels/', TravelAPI.as_view()),
    path('api/v1/travel/<int:pk>/', TravelDetailAPI.as_view()),

    path('api/v1/hotels/', HotelAPI.as_view()),
    path('api/v1/hotel/<int:pk>/', HotelDetailAPI.as_view()),

    path('api/v1/klasses/', KlassAPI.as_view()),
    path('api/v1/klass/<int:pk>/', KlassDetailAPI.as_view())
]


# Hech kimdan ko'chirganim yo'q doim o'zm bajaraman