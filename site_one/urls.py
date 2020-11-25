from django.urls import path
from . import views

app_name = 'site_one'
urlpatterns = [
    path('',views.index, name='index' ),
]