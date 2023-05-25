from django.contrib import admin
from .models import Product, Medicated_product, Non_medicated_product

admin.site.register(Product)
admin.site.register(Medicated_product)
admin.site.register(Non_medicated_product)