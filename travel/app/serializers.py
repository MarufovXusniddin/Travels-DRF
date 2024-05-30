from rest_framework import serializers
from .models import Travel, Klass, Hotel


class TravelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    description = serializers.CharField()
    term = serializers.CharField(max_length=50)
    klass_id = serializers.IntegerField()
    hotel_id = serializers.IntegerField()

    def create(self, validated_data):
        return Travel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.term = validated_data.get('term', instance.term)
        instance.klass_id = validated_data.get('klass_id', instance.klass_id)
        instance.hotel_id = validated_data.get('hotel_id', instance.hotel_id)
        instance.save()
        return instance


class HotelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    stars = serializers.IntegerField(default=0)
    price = serializers.FloatField(default=0)

    def create(self, validated_data):
        return Hotel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.stars = validated_data.get('stars', instance.stars)
        instance.price = validated_data.get('price', instance.price)


class KlassSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=100)
    price = serializers.FloatField(default=0)

    def create(self, validated_data):
        return Klass.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.price = validated_data.get('price', instance.price)




