from rest_framework import viewsets
from ..models.place import Place
from ..serializers.place import PlaceSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
