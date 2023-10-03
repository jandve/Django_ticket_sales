from rest_framework import serializers
from ..models.user import User
from .place import PlaceSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserPlacesSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    places = PlaceSerializer(many = True)

