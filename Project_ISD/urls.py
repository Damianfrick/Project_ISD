from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('site_one/', include('site_one.urls')),
    path('site_two/', include('site_two.urls')),
    path('site_three/', include('site_three.urls')),
    path('', include('site_home.urls')),
    path('site_four/', include('site_four.urls')),
    path('site_two/bbc/', include('site_two.urls')),
    path('site_two/google/', include('site_two.urls')),
    path('site_two/cnn/', include('site_two.urls'))
]