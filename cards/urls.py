from django.urls import path, include
from .views import test, UserViewSet, CardViewSet, SetViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('cards', CardViewSet)
router.register('sets', SetViewSet)

urlpatterns = [
    path('', test),
    path('', include(router.urls)),
]
