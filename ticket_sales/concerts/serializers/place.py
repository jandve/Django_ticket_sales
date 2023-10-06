from rest_framework import serializers
from ..models.place import Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"

class GroupPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Place
        fields = ("id", "name","capacity")