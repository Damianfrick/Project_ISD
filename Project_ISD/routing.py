from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import site_one.routing

""" linking the websocket with the site_one app routing"""

application=ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            site_one.routing.websocket_urlpatterns
        )
    )
})

