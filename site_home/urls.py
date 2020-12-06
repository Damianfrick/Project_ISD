from django.urls import path
from . import views

app_name = 'site_home'
urlpatterns = [
    path('',views.index, name='index' ),
    path('news/',views.news, name='news' ),
    path('contact/',views.contact, name='contact' ),
    path('about/',views.about, name='about' ),
]