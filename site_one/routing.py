from django.urls import re_path

from site_one import Consumer

"""websocket path: http upgrade (handshake) to ws"""

websocket_urlpatterns=[
    re_path(r'ws/library/(?P<room_name>\w+)/(?P<person_name>\w+)/$',Consumer.Consumer.as_asgi())
]