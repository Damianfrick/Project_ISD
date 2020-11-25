from django.urls import path
from . import views

app_name = 'site_home'
urlpatterns = [
    path('',views.index, name='index' ),
]