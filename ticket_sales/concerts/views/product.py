from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse
from ..models.product import Product
from ..serializers.product import ProductSerializer,ProductPlacesSerializer
from ..models.place import Place

class ProductViewSet(viewsets.ModelViewSet): 
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    @api_view(["GET"])
    def product_place(self, place_id):
        """
            return all the ticket for a given place
        """
        try:
            place = Place.objects.get(pk=place_id)
            ##places="Prueba"
            products=Product.objects.filter(place_id=place_id)
            return JsonResponse(ProductPlacesSerializer({
                "place": place,
                "products": products,
                "count": products.count(),
            }).data, status=202)
        except Exception as e:
            ##logger.error(f'something when wrong fetching the user with id: {user_id} places')
            return JsonResponse({"message": str(e)}, safe=False, status=400)