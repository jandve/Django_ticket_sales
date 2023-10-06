from rest_framework import serializers
from ..models.product import Product
from .place import PlaceSerializer,GroupPlaceSerializer
from django.http import JsonResponse
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

class ProductPlacesSerializer(serializers.Serializer):
    ##place = GroupPlaceSerializer(many = True)
    place=GroupPlaceSerializer()
    count = serializers.IntegerField()
    products = ProductSerializer(many = True)