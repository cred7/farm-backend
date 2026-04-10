# from .views import farm_summary, add_farm_activity
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmViewSet, FarmPointViewSet

router = DefaultRouter()
router.register(r"farms", FarmViewSet, basename="farm")
router.register(r"farm-points", FarmPointViewSet, basename="farm-points")

urlpatterns = [
    path("", include(router.urls)),
]

# urlpatterns += [
#     path('farms/<int:farm_id>/summary/', farm_summary),
#     path('farms/<int:farm_id>/activity/', add_farm_activity),
# ]
