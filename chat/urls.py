from .consumer import WebSocketConsumer
from django.urls import path, include

websocket_urlpatterns = [
    path(r'^ui-channel$', WebSocketConsumer),
]