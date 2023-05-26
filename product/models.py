from django.db import models

class Product(models.Model):
    quantity = models.PositiveIntegerField('Количество')
    cost = models.DecimalField('Стоимость', decimal_places=2, max_digits=15)

    def get_absolute_url(self):
        return f'/'

class Medicated_product(models.Model):
    name = models.CharField('Наименование', max_length=50)
    manufacturer = models.CharField('Производитель', max_length=100)
    formative_group = models.CharField('Фармакологическая группа', max_length=50)
    pharmaceutical_form = models.CharField('Лекарственная форма', max_length=15)
    dosage = models.CharField('Дозировка', max_length=30) #+ед.измер
    volume_in_package = models.CharField('Количество в упаковке', max_length=15) #+ед.измер
    sales_condition = models.CharField('Условия отпуска', max_length=50)
    description = models.TextField('Описание')
    production_date = models.DateField('Дата производства', null=False)
    shelf_life = models.PositiveIntegerField('Срок годности')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True, unique=True)

    def get_absolute_url(self):
        return f'/'

class Non_medicated_product(models.Model):
    name = models.CharField('Наименование', max_length=50)
    manufacturer = models.CharField('Производитель', max_length=100)
    category = models.CharField('Категория', max_length=50)
    volume_in_package = models.CharField('Количество в упаковке', max_length=15)  # +ед.измер
    production_date = models.DateField('Дата производства', null=False)
    shelf_life = models.PositiveIntegerField('Срок годности', null=True, blank=999)
    guarantee = models.PositiveIntegerField('Срок гарантии', null=True, blank=999)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True, unique=True)

    def get_absolute_url(self):
        return f'/product'
