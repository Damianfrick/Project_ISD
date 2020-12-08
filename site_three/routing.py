from django.urls import re_path

from site_three import Consumer

websocket_urlpatterns=[
    re_path(r'ws/site_three/(?P<room_name>\w+)/(?P<person_name>\w+)/$',Consumer.Consumer.as_asgi())
]