from . import views
from django.urls import path

#created two paths, which handel the chat request /site_one/ (gonna change it to library soon)
#second path which leads to site_two/room/ input:language / input: username ===> chatscreen

urlpatterns=[
    path('',views.ShowChatHome,name='showchat'),
    path('room/<str:room_name>/<str:person_name>', views.ShowChatPage, name='showchat'),
]