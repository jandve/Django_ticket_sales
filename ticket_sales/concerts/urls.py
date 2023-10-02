from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.product import ProductViewSet
from .views.user import UserViewSet
from .views.place import PlaceViewSet

router=DefaultRouter()
router.register(r"product", ProductViewSet)
router.register(r"user", UserViewSet)
router.register(r"place", PlaceViewSet)

urlpatterns=[
    path("product",ProductViewSet.as_view({'get': 'list'}) , name="product"),
    path("user", UserViewSet.as_view({'get': 'list'}), name="user"),
    path("place", PlaceViewSet.as_view({'get': 'list'}), name="place"),
    path('',include(router.urls))
]