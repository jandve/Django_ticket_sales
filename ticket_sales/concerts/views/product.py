from rest_framework import viewsets
from ..models.product import Product
from ..serializers.product import ProductSerializer
from django.http import HttpResponse, JsonResponse

class ProductViewSet(viewsets.ModelViewSet): 
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def getProducts():
        return HttpResponse(f"Bienvenido a la clase de Django")
    