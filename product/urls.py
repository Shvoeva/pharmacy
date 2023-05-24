from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product'),
    path('purchase', views.purchase, name='purchase')
]