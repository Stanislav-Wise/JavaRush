from django.urls import path
from .views import home, contacts, product_list, product_detail, all_categories, category_detail


urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>', product_detail, name='product_detail'),
    path('categories/', all_categories, name='all_categories'),
    path('categories/<int:category_id>', category_detail, name='category_detail'),
]