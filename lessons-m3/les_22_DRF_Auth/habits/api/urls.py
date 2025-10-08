from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from .views import HabitListCreateApiView, HabitListCreateApiView, HabitRetrieveUpdateDestroyAPIView
from .views import  HabitViewSet


app_name = 'habits'
router = DefaultRouter()

router.register(
    r"",
    HabitViewSet,
    basename="habits",
)

urlpatterns = [
    # path('', HabitListCreateApiView.as_view(), name='list_create'),
    # path('<int:pk>/', HabitRetrieveUpdateDestroyAPIView.as_view(), name='detail'),
    path("", include(router.urls))
]

# urlpatterns += [path("", include(router.urls))]