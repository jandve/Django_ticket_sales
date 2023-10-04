from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from ..models.band import Band
from ..models.product import Product
from ..serializers.band import BandSerializer, BandProductsSerializer
from django.http import JsonResponse

class BandViewSet(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

@api_view(['GET'])
def band_product(bandId):
    try: 
        product = Product.objects.filter(bandId = bandId)
        return JsonResponse(BandProductsSerializer({
            "product": product,
            "count": product.count(),
        }))
    except Band.DoesNotExist: 
        return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND) 

