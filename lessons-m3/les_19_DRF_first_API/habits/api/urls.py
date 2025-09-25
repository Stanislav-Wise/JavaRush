from django.urls import path
from .views import HabitListCreateApiView

app_name = 'habits'

urlpatterns = [
    path('', HabitListCreateApiView.as_view(), name='list_create'),
]