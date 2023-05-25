from django.shortcuts import render
from .models import Product, Medicated_product, Non_medicated_product
from purchase.models import Purchase, Purchase_item

def index(request):
    products = Product.objects.all()
    medicated_products = Medicated_product.objects.all()
    non_medicated_products = Non_medicated_product.objects.all()
    return render(request, 'product/index.html', {'products': products,
                  'medicated_products': medicated_products,
                  'non_medicated_products': non_medicated_products})

def purchase(request):
    products = Product.objects.all()
    medicated_products = Medicated_product.objects.all()
    non_medicated_products = Non_medicated_product.objects.all()
    purchases = Purchase.objects.all()
    purchase_items = Purchase_item.objects.all()
    return render(request, 'purchase/index.html', {'products': products,
                  'medicated_products': medicated_products,
                  'non_medicated_products': non_medicated_products,
                  'purchases': purchases,
                  'purchase_items': purchase_items})