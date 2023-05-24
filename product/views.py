from django.shortcuts import render

def index(request):
    return render(request, 'product/index.html')

def purchase(request):
    return render(request, 'purchase/index.html')