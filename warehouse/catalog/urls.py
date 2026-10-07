from django.urls import path
from .views import home, products, about

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('about/', about, name='about'),
]