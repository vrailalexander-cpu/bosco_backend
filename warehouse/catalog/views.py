from django.shortcuts import render, redirect
from django.contrib import messages
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

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        size = request.POST.get('size')
        color = request.POST.get('color')
        price = request.POST.get('price')

        Product.objects.create(
            name=name,
            brand=brand,
            size=size,
            color=color,
            price=price
        )

        messages.success(request, 'Товар успішно додано!')

        return redirect('products')

    return render(request, 'catalog/add_product.html')