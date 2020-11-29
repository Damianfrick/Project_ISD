from django.urls import re_path

from Project_ISD import Consumer

websocket_urlpatterns=[
    re_path(r'ws/site_one/(?P<person_name>\w+)/$',Consumer.Consumer.as_asgi())
]