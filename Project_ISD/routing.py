from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import site_one.routing

application=ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            site_one.routing.websocket_urlpatterns
        )
    )
})

