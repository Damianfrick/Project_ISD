"""from django.urls import path
from . import views

app_name = 'site_three'
urlpatterns = [
    path('',views.index, name='index' ),
]
"""

from . import views
from django.urls import path

urlpatterns=[
    path('',views.ShowChatHome,name='showchat'),
    path('room/<str:room_name>/<str:person_name>', views.ShowChatPage, name='showchat'),
]