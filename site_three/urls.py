"""from django.urls import path
from . import views

app_name = 'site_three'
urlpatterns = [
    path('',views.index, name='index' ),
]
"""

#created two paths, which handel the chat request /site_one/ (gonna change it to library soon)
#second path which leads to site_two/room/ input:language / input: username ===> chatscreen

from . import views
from django.urls import path

urlpatterns=[
    path('',views.ShowChatHome,name='showchat'),
    path('room/<str:room_name>/<str:person_name>', views.ShowChatPage, name='showchat'),
]