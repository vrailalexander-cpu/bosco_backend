from django.urls import path
from .views import home, products, about, add_product

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('about/', about, name='about'),
    path('products/add/', add_product, name='add_product'),
]