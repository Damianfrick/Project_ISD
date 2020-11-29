from django.urls import re_path

from site_one import Consumer

websocket_urlpatterns=[
    re_path(r'ws/site_one/(?P<person_name>\w+)/$',Consumer.Consumer.as_asgi())
]