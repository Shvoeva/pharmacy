from django.db import models
from product.models import Product

class Purchase(models.Model):
    date_and_time = models.DateTimeField('Дата и время', null=False)
    till_number = models.PositiveIntegerField('Номер кассы')
    pharmacist = models.CharField('ФИО фармацевта', max_length=50)
    amount = models.DecimalField('Сумма к оплате', decimal_places=2, max_digits=15, null=True, blank=0)

    def get_absolute_url(self):
        return f'/purchase/'

class Purchase_item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Количество')
    amount = models.DecimalField('Стоимость', decimal_places=2, max_digits=15, null=True, blank=0)

    def get_absolute_url(self):
        return f'/purchase/'
