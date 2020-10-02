from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet,listingViewSet,UserViewSet


router = routers.DefaultRouter()
router.register('product',ProductViewSet)
router.register('listing',listingViewSet)
router.register('users',UserViewSet)


urlpatterns = [
    path('',include(router.urls))
]