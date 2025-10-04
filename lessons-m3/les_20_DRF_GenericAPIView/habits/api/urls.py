from django.urls import path
# from .views import HabitListCreateApiView
from .views import HabitListCreateApiView, HabitRetrieveUpdateDestroyAPIView


app_name = 'habits'

urlpatterns = [
    path('', HabitListCreateApiView.as_view(), name='list_create'),
    path('<int:pk>/', HabitRetrieveUpdateDestroyAPIView.as_view(), name='detail'),
]