from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Будет ссылка на маршруты как 'blog_api:<name>'
app_name = 'blog_api'


urlpatterns = [
    # POST /api/v1/token/
    # В теле {JSON } запроса у нас будет email и password
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # POST /api/v1/token/refresh/
    # В теле {JSON} запроса у нас будет refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]