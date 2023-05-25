from django.shortcuts import render
from .models import Product, Medicated_product, Non_medicated_product
from purchase.models import Purchase, Purchase_item
from .forms import ProductForm, Medicated_productForm, Non_medicated_productForm, Purchase_itemForm, PurchaseForm
from django.views.generic import UpdateView, DeleteView
from django.shortcuts import render

class PurchaseUpdateView(UpdateView):
    model = Purchase
    template_name = 'purchase/update_purchase.html'

    form_class = PurchaseForm

class PurchaseDeleteView(DeleteView):
    model = Purchase
    success_url = '/purchase/'
    template_name = 'purchase/delete_purchase.html'

class PurchaseItemUpdateView(UpdateView):
    model = Purchase_item
    template_name = 'purchase/update_purchase_item.html'

    form_class = Purchase_itemForm

class PurchaseItemDeleteView(DeleteView):
    model = Purchase_item
    success_url = '/purchase/'
    template_name = 'purchase/delete_purchase_item.html'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/update_product.html'

    form_class = ProductForm

class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/'
    template_name = 'product/delete_product.html'

class MedicatedProductUpdateView(UpdateView):
    model = Medicated_product
    template_name = 'product/update_medicated_product.html'

    form_class = Medicated_productForm

class MedicatedProductDeleteView(DeleteView):
    model = Medicated_product
    success_url = '/'
    template_name = 'product/delete_product.html'

class NonMedicatedProductUpdateView(UpdateView):
    model = Non_medicated_product
    template_name = 'product/update_non_medicated_product.html'

    form_class = Non_medicated_productForm

class NonMedicatedProductDeleteView(DeleteView):
    model = Non_medicated_product
    success_url = '/product/'
    template_name = 'product/delete_product.html'

def update_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()

    purchase = Purchase.objects.all()

    form = PurchaseForm()

    return render(request, 'product/pdate_purchase.html', {'purchase': purchase, 'form': form})

def update_purchase_item(request):
    if request.method == 'POST':
        form = Purchase_itemForm(request.POST)
        if form.is_valid():
            form.save()

    item = Purchase_item.objects.all()

    form = Purchase_itemForm()

    return render(request, 'product/update_purchase_item.html', {'item': item, 'form': form})

def update_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

    products = Product.objects.all()

    form = ProductForm()

    return render(request, 'product/update_product.html', {'products': products, 'form': form})

def update_medicated_product(request):
    if request.method == 'POST':
        form = Medicated_productForm(request.POST)
        if form.is_valid():
            form.save()

    products = Medicated_product.objects.all()

    form = Medicated_productForm()

    return render(request, 'product/update_medicated_product.html', {'products': products, 'form': form})

def update_non_medicated_product(request):
    if request.method == 'POST':
        form = Non_medicated_productForm(request.POST)
        if form.is_valid():
            form.save()

    products = Non_medicated_product.objects.all()

    form = Non_medicated_productForm()

    return render(request, 'product/update_non_medicated_product.html', {'products': products, 'form': form})

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