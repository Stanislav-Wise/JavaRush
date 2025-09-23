from django.urls import path
from .api import PingAPIView


app_name = 'habits'

urlpatterns = [
    path('ping/', PingAPIView.as_view(), name='ping'),
]