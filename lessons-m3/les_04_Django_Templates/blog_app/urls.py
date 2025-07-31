from django.urls import path
from .views import home, about, post_list, author_list


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('posts/', post_list, name='post_list'),
    path('authors/', author_list, name='author_list'),
]
