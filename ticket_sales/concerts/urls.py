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
    path("user", UserViewSet.as_view({'get': 'list', 'post': 'create', 'patch':'partial_update', 'put': 'update', 'delete': 'destroy'}), name="user"),
    path("user/<str:user_id>/place", UserViewSet.user_place, name="user-places"),
    path("product",ProductViewSet.as_view({'get': 'list'}) , name="product"),
    path("product/<str:place_id>/place", ProductViewSet.product_place, name="product-places"),
    path("place", PlaceViewSet.as_view({'get': 'list', 'post': 'create', 'patch':'partial_update', 'put': 'update', 'delete': 'destroy'}), name="place"),
    path('',include(router.urls))
]