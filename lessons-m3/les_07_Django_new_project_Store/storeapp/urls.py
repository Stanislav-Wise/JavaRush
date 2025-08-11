from django.urls import path
from .views import home, contacts, product_list, product_detail


urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products', product_list, name='product_list'),
    path('products/<int:product_id>', product_detail, name='product_detail'),
]