from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse
import logging
from ..models.user import User
from ..models.place import Place
from ..serializers.user import UserSerializer, UserPlacesSerializer

logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @api_view(["GET"])
    def user_place(self, user_id):
        """
            return all the places for a given user
        """
        try:
            places = Place.objects.filter(user_id=user_id)
            return JsonResponse(UserPlacesSerializer({
                "places": places,
                "count": places.count(),
            }).data, status=202)
        except Exception as e:
            logger.error(f'something when wrong fetching the user with id: {user_id} places')
            return JsonResponse({"message": str(e)}, safe=False, status=400)
