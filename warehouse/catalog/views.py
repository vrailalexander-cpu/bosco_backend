from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'catalog/home.html')

def products(request):
    products = Product.objects.all()

    return render(
        request,
        'catalog/products.html',
        {'products': products}
    )

def about(request):
    return render(request, 'catalog/about.html')