from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/update_purchase', views.PurchaseUpdateView.as_view(), name='purchase-update'),
    path('<int:pk>/delete_purchase', views.PurchaseDeleteView.as_view(), name='purchase-delete'),

    path('<int:pk>/update_purchase_item', views.PurchaseItemUpdateView.as_view(),
         name='purchase-item-update'),
    path('<int:pk>/delete_purchase_item', views.PurchaseItemDeleteView.as_view(),
         name='purchase-item-delete'),

    path('<int:pk>/update_product', views.ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete_product', views.ProductDeleteView.as_view(), name='product-delete'),

    path('<int:pk>/update_medicated_product', views.MedicatedProductUpdateView.as_view(),
         name='medicated-product-update'),
    path('<int:pk>/delete_medicated_product', views.MedicatedProductDeleteView.as_view(),
         name='medicated-product-delete'),

    path('<int:pk>/update_non_medicated_product', views.NonMedicatedProductUpdateView.as_view(),
         name='non-medicated-product-update'),
    path('<int:pk>/delete_non_medicated_product', views.NonMedicatedProductDeleteView.as_view(),
         name='non-medicated-product-delete'),

    path('', views.index, name='product'),
    path('product', views.index2, name='product2'),
    path('purchase', views.purchase, name='purchase')
]