from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import site_one.routing
import site_three.routing

application=ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            site_one.routing.websocket_urlpatterns
        )
    )
})

application=ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            site_three.routing.websocket_urlpatterns
        )
    )
})