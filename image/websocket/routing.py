from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/farm/<int:farm_id>/", consumers.FarmConsumer.as_asgi()),
]
