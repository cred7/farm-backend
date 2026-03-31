from rest_framework import serializers
from .models import Farm, FarmPoint


class FarmPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmPoint
        fields = ['id', 'latitude', 'longitude']


class FarmSerializer(serializers.ModelSerializer):
    points = FarmPointSerializer(many=True, read_only=True)

    class Meta:
        model = Farm
        fields = ['id', 'name', 'created_at', 'points']
