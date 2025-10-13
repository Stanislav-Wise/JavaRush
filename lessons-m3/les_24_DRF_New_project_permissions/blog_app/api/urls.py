from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from blog_app.api.views import PostViewSet

# Будет ссылка на маршруты как 'blog_api:<name>'
app_name = 'blog_api'

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')


urlpatterns = [
    # POST /api/v1/token/
    # В теле {JSON } запроса у нас будет email и password
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # POST /api/v1/token/refresh/
    # В теле {JSON} запроса у нас будет refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls