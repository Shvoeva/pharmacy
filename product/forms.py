from .models import *
from purchase.models import *
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, NumberInput, DateInput, Select, modelform_factory

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['quantity', 'cost']

        widgets = {
            "quantity": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество'
            }),
            "cost": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость'
            })
        }

class Medicated_productForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].empty_label = 'Ссылка на товар не выбрана'

    class Meta:
        model = Medicated_product
        fields = ['name', 'manufacturer', 'formative_group', 'pharmaceutical_form',
                  'dosage', 'volume_in_package', 'sales_condition', 'description',
                  'production_date', 'shelf_life', 'product']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование'
            }),
            "manufacturer": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Производитель'
            }),
            "formative_group": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фармакологическая группа'
            }),
            "pharmaceutical_form": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Лекарственная форма'
            }),
            "dosage": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дозировка'
            }),
            "volume_in_package": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество в упаковке'
            }),
            "sales_condition": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Условия отпуска'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "production_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата производства'
            }),
            "shelf_life": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Срок годности'
            }),
            "product": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на товар'
            })
        }

class Non_medicated_productForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].empty_label = 'Ссылка на товар не выбрана'

    class Meta:
        model = Non_medicated_product
        fields = ['name', 'manufacturer', 'category', 'volume_in_package',
                  'production_date', 'shelf_life', 'guarantee', 'product']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование'
            }),
            "manufacturer": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Производитель'
            }),
            "category": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Категория'
            }),
            "volume_in_package": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество в упаковке'
            }),
            "production_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата производства'
            }),
            "shelf_life": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Срок годности'
            }),
            "guarantee": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Срок гарантии'
            }),
            "product": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на товар'
            })
        }

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ['date_and_time', 'till_number', 'pharmacist', 'amount']

        widgets = {
            "date_and_time": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время продажи'
            }),
            "till_number": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер кассы'
            }),
            "pharmacist": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО фармацевта'
            }),
            "amount": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Итоговая сумма'
            })
        }

class Purchase_itemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].empty_label = 'Ссылка на товар не выбрана'
        self.fields['purchase'].empty_label = 'Ссылка на продажу не выбрана'

    class Meta:
        model = Purchase_item
        fields = ['product', 'purchase', 'quantity', 'amount']

        widgets = {
            "product": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на товар'
            }),
            "purchase": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на продажу'
            }),
            "quantity": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество'
            }),
            "amount": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость за все количество'
            })
        }