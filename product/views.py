from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'product/index.html')

def purchase(request):
    return HttpResponse('<h4>Purchase</h4>')