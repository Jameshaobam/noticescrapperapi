from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/123/', admin.site.urls),
    path('',include('scrapper.urls')),
    path('notice/',include('extranotice.urls')),
]
