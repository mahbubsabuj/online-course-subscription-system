from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('main.urls',namespace='main')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
