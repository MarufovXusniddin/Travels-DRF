from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Travel, Klass, Hotel
from .serializers import TravelSerializer, KlassSerializer, HotelSerializer

# Create your views here.


class TravelAPI(APIView):
    def get(self, request, pk=None):
        if pk is None:
            travels = Travel.objects.all()
            return Response({'travels': TravelSerializer(travels, many=Travel).data})
        else:
            try:
                travel = Travel.objects.get(pk=pk)
                return Response({'travel': TravelSerializer(travel).data})
            except:
                return Response({"error": "Bu id da maqola mavjud emas!"})

    def post(self, request):
        serializer = TravelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        travels = serializer.save()
        return Response({'travels': TravelSerializer(travels).data})

    def put(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Method \"PUT\" not allowed."})
        try:
            travels = Travel.objects.get(pk=pk)
            serializer = TravelSerializer(travels, data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_travel = serializer.save()
            return Response({'news': TravelSerializer(updated_travel).data})
        except:
            return Response({'error': "Bu id da maqola mavjud emas"})

    def delete(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Method \"DELETE\" not allowed."})
        try:
            travel = Travel.objects.get(pk=pk)
            travel.delete()
            return Response({'success': "Maqola o'chirildi"})
        except:
            return Response({'error': "Bu id da maqola mavjud emas"})


class HotelAPI(APIView):
    def get(self, request, pk=None):
        if pk is None:
            hotels = Hotel.objects.all()
            return Response({"hotels": HotelSerializer(hotels, many=True).data})
        else:
            try:
                hotel = Hotel.objects.get(pk=pk)
                return Response({"hotel": HotelSerializer(hotel).data})
            except:
                return Response({"error": "Bu id da maqola mavjud emas!"})

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        hotel = serializer.save()
        return Response({"hotel": HotelSerializer(hotel).data})

    def put(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Method \"PUT\" not allowed."})
        else:
            try:
                hotel = Hotel.objects.get(pk=pk)
                serializer = HotelSerializer(hotel, data=request.data)
                serializer.is_valid()
                updated_hotel = serializer.save()
                return Response({"hotel": HotelSerializer(updated_hotel).data})
            except:
                return Response({"error": "Bu id da maqola mavjud emas!"})

    def delete(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Method \"DELETE\" not allowed."})
        else:
            try:
                hotel = Hotel.objects.get(pk=pk)
                hotel.delete()
                return Response({"success": "Maqola o'chirildi !"})
            except:
                return Response({"Bu id da maqola mavjud emas!"})


class KlassAPI(APIView):
    def get(self, request, pk=None):
        if pk is None:
            klasses = Klass.objects.all()
            return Response({"klasses": HotelSerializer(klasses, many=True).data})
        else:
            try:
                klass = Klass.objects.get(pk=pk)
                return Response({"klass": HotelSerializer(klass).data})
            except:
                return Response({"error": "Bu id da maqola mavjud emas!"})

    def post(self, request):
        serializer = KlassSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        klass = serializer.save()
        return Response({"hotel": HotelSerializer(klass).data})

    def put(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Method \"PUT\" not allowed."})
        else:
            try:
                klass = Klass.objects.get(pk=pk)
                serializer = HotelSerializer(klass, data=request.data)
                serializer.is_valid()
                updated_klass = serializer.save()
                return Response({"hotel": HotelSerializer(updated_klass).data})
            except:
                return Response({"error": "Bu id da maqola mavjud emas!"})

    def delete(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Method \"DELETE\" not allowed."})
        else:
            try:
                klass = Klass.objects.get(pk=pk)
                klass.delete()
                return Response({"success": "Maqola o'chirildi !"})
            except:
                return Response({"Bu id da maqola mavjud emas!"})