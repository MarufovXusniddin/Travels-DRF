from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import mixins
from rest_framework import generics
from .models import Travel, Klass, Hotel
from .serializers import TravelSerializer, KlassSerializer, HotelSerializer


# Create your views here.


class TravelAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TravelDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class HotelAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class HotelDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin,
                                              mixins.UpdateModelMixin,
                                              mixins.DestroyModelMixin):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class KlassAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class KlassDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)