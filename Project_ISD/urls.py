from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('site_one.urls')),
    path('coffeeshop/', include('site_two.urls')),
    path('bar/', include('site_three.urls')),
    path('', include('site_home.urls')),
    path('covidinfo/', include('site_four.urls')),
    path('coffeeshop/bbc/', include('site_two.urls')),
    path('coffeeshop/google/', include('site_two.urls')),
    path('coffeeshop/cnn/', include('site_two.urls'))
]