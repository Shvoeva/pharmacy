from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/update', views.ProductUpdateView.as_view(), name='product-update'),
    path('', views.index, name='product'),
    path('product', views.index2, name='product2'),
    path('purchase', views.purchase, name='purchase')
]