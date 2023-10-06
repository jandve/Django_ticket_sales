from rest_framework import serializers
from ..models.band import Band
from .product import ProductSerializer

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = "__all__"

class BandProductsSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    products = ProductSerializer(many = True)
