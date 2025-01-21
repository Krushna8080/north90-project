from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),                 # Admin page
    path("", include("chat.urls")),                  # Include chat app URLs as the default route
]
