
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from chat.urls import websocket_urlpatterns


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
    })