from django.urls import path
from . import views


app_name = 'site_two'
urlpatterns = [
    path('',views.index, name='index' ),
    path('bbc/', views.bbc, name='BBC'),
    path('google/', views.google, name='Google'),
    path('cnn/', views.cnn, name='CNN')
]