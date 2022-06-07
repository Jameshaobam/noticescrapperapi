from django.urls import path
from .views import ShowNoticesApiView  
urlpatterns = [
    path("api/v2/extra-notice/",ShowNoticesApiView.as_view(),name="EXTRANOTICE"),
]
