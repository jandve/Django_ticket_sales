from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.product import ProductViewSet  

router=DefaultRouter()
router.register(r"products",ProductViewSet)

urlpatterns=[
    path("product/",ProductViewSet.getProducts , name="product"),
    path('',include(router.urls))
]