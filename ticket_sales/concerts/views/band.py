from rest_framework import viewsets
from rest_framework.decorators import api_view
from ..models.band import Band
import logging
from ..models.product import Product
from ..serializers.band import BandSerializer, BandProductsSerializer
from django.http import  JsonResponse

logger = logging.getLogger(__name__)

class BandViewSet(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

    @api_view(['GET'])
    def band_product(self, band_id):
        """
        Products according to the band
        """
        try: 
            products = Product.objects.filter(band_id=band_id)
            logger.error(f' ===> : {list(products)}')
            return JsonResponse(BandProductsSerializer({
                "products": products,
                "count": products.count(),
            }).data, status=202)
        except Exception as e:
            logger.error(f'something went wrong fetching the band with id: {band_id} products')
            return JsonResponse({"message": str (e)}, status=500, safe=False)