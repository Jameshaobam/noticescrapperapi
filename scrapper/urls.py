from django.urls import path
from . import  views
urlpatterns = [
    path('api/v1/MU',views.scrape_mu,name='MU'),
    path('api/v1/mit-syllabus',views.scrape_mit_syllabus,name='MITSYLLABUS'),
    path('',views.home,name='home'),
]
