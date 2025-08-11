from django.shortcuts import render
from .models import Product, Category


def home(request):
    return render(request, 'storeapp/index.html')


def contacts(request):
    return render(request, 'storeapp/index.html')


def product_list(request):
    return render(request, 'storeapp/index.html')


def product_detail(request, product_id):
    return render(request, 'storeapp/index.html')

