from rest_framework import viewsets
from rest_framework.decorators import api_view
from ..models.band import Band
from ..models.product import Product
from ..serializers.band import BandSerializer, BandProductsSerializer
from django.http import  JsonResponse

class BandViewSet(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

    @api_view(['GET'])
    def band_product(self, band_id):
        """
        Products according to the band
        """
        try: 
            product = Product.objects.filter(band_id=band_id)
            return JsonResponse(BandProductsSerializer({
                "product": product,
                "count": product.count(),
            }))
        except Exception as e:
            return JsonResponse({"message": str (e)}, status=500, safe=False)