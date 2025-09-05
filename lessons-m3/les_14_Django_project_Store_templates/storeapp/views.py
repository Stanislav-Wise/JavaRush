from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import render, get_object_or_404, redirect


def home(request):
    return render(request, 'storeapp/index.html')


def contacts(request):
    return render(request, 'storeapp/contacts.html')


def product_list(request):
    products = Product.objects.all()
    context = {
        'title': 'Product list',
        'products': products
    }
    return render(request, 'storeapp/product_list.html', context=context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # category = Category.objects.filter(post=detail)

    context = {
        'title': 'Product detail',
        'product': product,
        #'comments': comments,
        #'tags': tags
    }
    return render(request, 'storeapp/product_detail.html', context = context)


def all_categories(request):
    categories = Category.objects.all()
    context = {
        'title': 'Category list',
        'categories': categories
    }
    return render(request, 'storeapp/all_categories.html', context=context)


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    # category = Category.objects.filter(post=detail)

    context = {
        'title': 'category detail',
        'category': category,
        #'comments': comments,
        #'tags': tags
    }
    return render(request, 'storeapp/category_detail.html', context = context)