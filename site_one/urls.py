from . import views
from django.urls import path

urlpatterns=[
    path('',views.ShowChatHome,name='showchat'),
    path('room/<str:person_name>', views.ShowChatPage, name='showchat'),
]