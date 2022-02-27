from django.urls import path
from . import  views
urlpatterns = [
    path('api/v1/MU',views.scrape_mu,name='MU'),
    path('',views.home,name='home'),
]
