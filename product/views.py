from django.shortcuts import render
from .models import Product, Medicated_product, Non_medicated_product
from purchase.models import Purchase, Purchase_item
from .forms import ProductForm, Medicated_productForm, Non_medicated_productForm, Purchase_itemForm, PurchaseForm
from django.views.generic import UpdateView

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/update_product.html'

    form_class = ProductForm

def update_product(request):
    if request.method == 'POST':
        pform = ProductForm(request.POST)
        if pform.is_valid():
            pform.save()

    if request.method == 'POST':
        mform = Medicated_productForm(request.POST)
        if mform.is_valid():
            mform.save()

    products = Product.objects.all()
    medicated_products = Medicated_product.objects.all()

    pform = ProductForm()
    mform = Medicated_productForm()

    return render(request, 'product/update_product.html', {'products': products, 'medicated_products': medicated_products,
                                                  'pform': pform, 'mform': mform})

def index(request):
    if request.method == 'POST':
        pform = ProductForm(request.POST)
        if pform.is_valid():
            pform.save()

    if request.method == 'POST':
        mform = Medicated_productForm(request.POST)
        if mform.is_valid():
            mform.save()

    products = Product.objects.all()
    medicated_products = Medicated_product.objects.all()

    pform = ProductForm()
    mform = Medicated_productForm()

    return render(request, 'product/index.html', {'products': products, 'medicated_products': medicated_products,
                                                  'pform': pform, 'mform': mform})

def index2(request):
    if request.method == 'POST':
        pform = ProductForm(request.POST)
        if pform.is_valid():
            pform.save()

    if request.method == 'POST':
        nform = Non_medicated_productForm(request.POST)
        if nform.is_valid():
            nform.save()

    products = Product.objects.all()
    non_medicated_products = Non_medicated_product.objects.all()

    pform = ProductForm()
    nform = Non_medicated_productForm()

    return render(request, 'product/index2.html', {'products': products,'non_medicated_products': non_medicated_products,
                                                  'pform': pform, 'nform': nform})

def purchase(request):
    if request.method == 'POST':
        pform = PurchaseForm(request.POST)
        if pform.is_valid():
            pform.save()

    if request.method == 'POST':
        iform = Purchase_itemForm(request.POST)
        if iform.is_valid():
            iform.save()

    products = Product.objects.all()
    medicated_products = Medicated_product.objects.all()
    non_medicated_products = Non_medicated_product.objects.all()
    purchases = Purchase.objects.all()
    purchase_items = Purchase_item.objects.all()

    pform = PurchaseForm()
    iform = Purchase_itemForm()

    return render(request, 'purchase/index.html', {'products': products, 'medicated_products': medicated_products,
                  'non_medicated_products': non_medicated_products, 'purchases': purchases,
                  'purchase_items': purchase_items, 'pform': pform, 'iform': iform})