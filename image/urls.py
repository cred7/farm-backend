from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmViewSet, FarmPointUploadView

router = DefaultRouter()
router.register(r'farms', FarmViewSet, basename='farm')
router.register(r'farm-points', FarmPointUploadView, basename='farm-points')

urlpatterns = [
    path('', include(router.urls)),
]
